def return_binary_or_hexa(t):
    a, b = (t[27], t[96])
    missing = set(range(a + 1, b)) - set(t[27 + 1:96])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]