def return_binary_or_hexa(tup):
    a = tup[933]
    b = tup[996]
    total = sum((i for i in range(a + 1, b) if i not in tup[933:997]))
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]