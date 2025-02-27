def return_binary_or_hexa(tup):
    a = tup[51]
    b = tup[76]
    range_set = set(tup[51:77])
    missing_nums = [x for x in range(a + 1, b) if x not in range_set]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]