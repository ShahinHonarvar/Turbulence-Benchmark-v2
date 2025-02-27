def return_binary_or_hexa(tup):
    a = tup[17]
    b = tup[88]
    missing = set(range(a + 1, b)) - set(tup[17 + 1:88])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]