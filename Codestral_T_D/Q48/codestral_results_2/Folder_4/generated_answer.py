def return_binary_or_hexa(t):
    a = t[49]
    b = t[74]
    missing = set(range(a + 1, b)) - set(t[49 + 1:74])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:].lstrip('0') if s else ''