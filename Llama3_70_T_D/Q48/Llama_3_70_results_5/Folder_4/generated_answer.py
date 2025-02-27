def return_binary_or_hexa(tup):
    a, b = (tup[49], tup[74])
    total = sum((i for i in range(a + 1, b) if i not in tup[50:74]))
    if total == 0:
        return ''
    if total % 2 == 0:
        return hex(total)[2:]
    return bin(total)[2:]