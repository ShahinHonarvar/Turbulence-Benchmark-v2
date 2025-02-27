def return_binary_or_hexa(t):
    a = t[62]
    b = t[96]
    s = sum(set(range(a + 1, b)) - set(t[63:96]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]