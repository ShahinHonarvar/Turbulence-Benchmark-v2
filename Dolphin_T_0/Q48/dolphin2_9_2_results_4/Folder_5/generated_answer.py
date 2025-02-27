def return_binary_or_hexa(t):
    a, b = (t[2], t[8])
    s = sum(set(range(a + 1, b)) - set(t[3:8]))
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]