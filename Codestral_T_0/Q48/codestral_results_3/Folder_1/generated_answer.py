def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    missing = set(range(a + 1, b)) - set(t[17 + 1:88])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]