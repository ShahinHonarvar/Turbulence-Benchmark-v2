def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    missing = set(range(a + 1, b)) - set(t[56:88])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]