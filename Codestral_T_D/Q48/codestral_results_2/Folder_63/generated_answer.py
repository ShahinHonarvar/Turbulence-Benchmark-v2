def return_binary_or_hexa(tup):
    a, b = (tup[81], tup[86])
    missing = set(range(a + 1, b)) - set(tup[81:86])
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]