def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    s = sum(set(range(a + 1, b)) - set(t[12:76]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]