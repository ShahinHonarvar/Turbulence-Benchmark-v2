def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[200]
    missing_nums = set(range(a + 1, b)) - set(tup[21:200])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]