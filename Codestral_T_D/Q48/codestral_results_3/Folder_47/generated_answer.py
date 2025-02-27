def return_binary_or_hexa(tup):
    a = tup[29]
    b = tup[53]
    missing = set(range(a + 1, b)) - set(tup[29 + 1:53])
    s = sum(missing)
    return bin(s)[2:] if s % 2 else hex(s)[2:]