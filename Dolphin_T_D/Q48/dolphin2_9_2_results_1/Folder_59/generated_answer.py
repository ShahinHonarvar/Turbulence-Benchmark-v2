def return_binary_or_hexa(t):
    a = t[0]
    b = t[10]
    s = sum(set(range(a + 1, b)) - set(t[1:10]))
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]