def return_binary_or_hexa(tup):
    a = tup[48]
    b = tup[76]
    missing = set(range(a + 1, b)).difference(tup[48:76])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:].lstrip('0') or '0'