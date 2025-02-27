def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[35]
    total = sum((i for i in range(a + 1, b) if i not in tup[20:36]))
    if total % 2 != 0:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''