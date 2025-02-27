def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[6]
    missing_nums = set(range(a + 1, b)) - set(tup[1:6])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]