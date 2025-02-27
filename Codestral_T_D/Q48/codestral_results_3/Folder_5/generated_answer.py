def return_binary_or_hexa(t):
    a, b = (t[2], t[8])
    s = sum(set(range(a + 1, b)) - set(t[3:8]))
    return bin(s)[2:] if s % 2 else hex(s)[2:] if s else ''