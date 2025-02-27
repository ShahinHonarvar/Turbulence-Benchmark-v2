def return_binary_or_hexa(t):
    a, b = (t[10], t[12])
    missing = set(range(a + 1, b)) - set(t[10:12])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]