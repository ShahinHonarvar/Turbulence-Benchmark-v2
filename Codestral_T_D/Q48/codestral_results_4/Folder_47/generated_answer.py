def return_binary_or_hexa(t):
    a, b = (t[29], t[53])
    missing = set(range(a + 1, b)) - set(t[29:54])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]