def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    missing = set(range(a + 1, b)) - set(t[6:8])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]