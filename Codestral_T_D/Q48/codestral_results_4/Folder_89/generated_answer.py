def return_binary_or_hexa(t):
    a, b = (t[55], t[84])
    missing = [x for x in range(a + 1, b) if x not in t[56:84]]
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:].upper() if s else ''