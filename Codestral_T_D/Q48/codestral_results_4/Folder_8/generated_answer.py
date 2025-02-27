def return_binary_or_hexa(tup):
    a, b = (tup[45], tup[48])
    missing = set(range(a + 1, b)) - set(tup[45 + 1:48])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]