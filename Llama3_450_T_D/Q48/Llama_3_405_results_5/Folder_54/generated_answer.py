def return_binary_or_hexa(tup):
    a = tup[35]
    b = tup[64]
    missing_nums = set(range(a + 1, b)) - set(tup[36:64])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]