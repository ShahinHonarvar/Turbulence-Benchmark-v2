def return_binary_or_hexa(t):
    a = t[3]
    b = t[8]
    s = sum(set([i for i in range(a + 1, b)]) - set(t[4:8]))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:]