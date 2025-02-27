def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    s = sum(set(range(a + 1, b)) - set(t[13:77]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]