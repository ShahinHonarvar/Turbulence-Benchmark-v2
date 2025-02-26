def return_binary_or_hexa(tup):
    a = tup[81]
    b = tup[86]
    missing_nums = [x for x in range(a + 1, b) if x not in tup[81:87]]
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]