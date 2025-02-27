def return_binary_or_hexa(tup):
    a, b = (tup[55], tup[84])
    missing = {i for i in range(a + 1, b) if i not in tup[55:85]}
    total = sum(missing)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()