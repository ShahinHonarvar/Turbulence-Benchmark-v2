def return_binary_or_hexa(t):
    a = t[36]
    b = t[54]
    s = sum(set(range(a + 1, b)) - set(t[37:54]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]