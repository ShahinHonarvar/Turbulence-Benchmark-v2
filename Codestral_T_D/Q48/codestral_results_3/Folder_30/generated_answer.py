def return_binary_or_hexa(tup):
    a, b = (tup[22], tup[24])
    present_nums = set(tup[22:24])
    missing_nums = set(range(a + 1, b))
    sum_missing = sum(missing_nums - present_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ''