def return_binary_or_hexa(t):
    a = t[80]
    b = t[200]
    s = sum(set([i for i in range(a + 1, b)]) - set(t[81:200]))
    if s % 2 == 0:
        return hex(s)[2:]
    else:
        return bin(s)[2:]