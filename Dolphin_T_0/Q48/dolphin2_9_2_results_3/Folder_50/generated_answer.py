def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    s = sum(range(a + 1, b)) - sum(t[14:76])
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]