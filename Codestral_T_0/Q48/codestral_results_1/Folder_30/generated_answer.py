def return_binary_or_hexa(t):
    a, b = (t[22], t[24])
    missing = set(range(a + 1, b)) - set(t[22:25])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]