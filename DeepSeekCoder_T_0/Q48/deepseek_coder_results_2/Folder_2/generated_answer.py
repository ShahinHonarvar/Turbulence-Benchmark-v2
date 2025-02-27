def return_binary_or_hexa(tup):
    a = tup[72]
    b = tup[93]
    range_set = set(range(a + 1, b))
    sub_set = set(tup[72:94])
    missing_numbers = range_set - sub_set
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
    return ''