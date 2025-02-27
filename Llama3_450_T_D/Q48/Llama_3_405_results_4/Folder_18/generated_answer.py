def return_binary_or_hexa(tup):
    a = tup[56]
    b = tup[90]
    nums = set(range(a + 1, b))
    tup_set = set(tup[57:90])
    missing_nums = nums - tup_set
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''