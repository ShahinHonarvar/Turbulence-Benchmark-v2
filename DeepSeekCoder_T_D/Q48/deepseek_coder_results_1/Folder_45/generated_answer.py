def return_binary_or_hexa(tup):
    a = tup[30]
    b = tup[200]
    range_set = set(range(a + 1, b))
    tup_set = set(tup[30:201])
    missing_numbers = range_set - tup_set
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
    return ''