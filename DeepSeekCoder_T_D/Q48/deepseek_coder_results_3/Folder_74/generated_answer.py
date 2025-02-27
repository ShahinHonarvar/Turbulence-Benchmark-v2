def return_binary_or_hexa(tup):
    a = tup[69]
    b = tup[97]
    range_set = set(range(a + 1, b))
    sub_tup = tup[69:98]
    missing_set = range_set - set(sub_tup)
    if not missing_set:
        return ''
    sum_missing = sum(missing_set)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]