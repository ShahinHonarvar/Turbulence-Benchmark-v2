def return_binary_or_hexa(t):
    a, b = (t[32], t[44])
    missing = set(range(a + 1, b)) - set(t[32 + 1:44])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]