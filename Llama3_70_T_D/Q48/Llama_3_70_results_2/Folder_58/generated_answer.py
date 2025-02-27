def return_binary_or_hexa(tup):
    a, b = (tup[275], tup[871])
    total = sum((i for i in range(a + 1, b) if i not in tup[275:872]))
    if total % 2 == 1:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''