def return_binary_or_hexa(tup):
    a = tup[86]
    b = tup[99]
    total = sum((i for i in range(a + 1, b) if i not in tup[86:100]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]