def return_binary_or_hexa(t):
    a, b = (t[56], t[90])
    missing = set(range(a + 1, b)) - set(t[56 + 1:90])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]