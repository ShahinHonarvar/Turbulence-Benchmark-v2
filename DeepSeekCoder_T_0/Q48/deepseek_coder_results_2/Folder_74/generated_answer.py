def return_binary_or_hexa(tup):
    a = tup[69]
    b = tup[97]
    range_set = set(range(a + 1, b))
    subset = set(tup[69:98])
    missing = range_set - subset
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]