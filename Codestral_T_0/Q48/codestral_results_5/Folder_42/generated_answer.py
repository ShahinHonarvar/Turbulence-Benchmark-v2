def return_binary_or_hexa(t):
    a, b = (t[18], t[60])
    missing = set(range(a + 1, b)) - set(t[18 + 1:60])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]