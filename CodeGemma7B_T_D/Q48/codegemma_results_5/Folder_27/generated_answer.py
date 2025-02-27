def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[89]
    x = set(tup[86:89])
    y = sum((i for i in range(a + 1, b) if i not in x))
    if y % 2:
        return bin(y)[2:]
    return hex(y)[2:].upper()