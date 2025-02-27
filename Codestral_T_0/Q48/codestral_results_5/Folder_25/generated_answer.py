def return_binary_or_hexa(t):
    a, b = (t[37], t[43])
    missing = set(range(a + 1, b)) - set(t[37 + 1:43])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]