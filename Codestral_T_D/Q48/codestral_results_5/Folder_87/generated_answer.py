def return_binary_or_hexa(tup):
    a, b = (tup[20], tup[43])
    missing = set(range(a + 1, b)) - set(tup[20:43])
    total = sum(missing)
    return bin(total)[2:] if total % 2 else hex(total)[2:]