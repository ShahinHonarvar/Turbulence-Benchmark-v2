def return_binary_or_hexa(tup):
    a, b = (tup[39], tup[43])
    total = sum((i for i in range(a + 1, b) if i not in tup[39:44]))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]