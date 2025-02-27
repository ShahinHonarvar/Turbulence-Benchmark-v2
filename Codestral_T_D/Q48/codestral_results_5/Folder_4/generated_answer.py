def return_binary_or_hexa(tup):
    a, b = (tup[49], tup[74])
    s = sum(set(range(a + 1, b)) - set(tup[49 + 1:74]))
    return bin(s)[2:] if s % 2 else hex(s)[2:]