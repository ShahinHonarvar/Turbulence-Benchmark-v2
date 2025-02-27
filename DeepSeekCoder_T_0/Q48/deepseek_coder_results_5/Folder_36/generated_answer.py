def return_binary_or_hexa(tup):
    a = tup[110]
    b = tup[348]
    range_set = set(range(a + 1, b))
    tup_set = set(tup[110:349])
    missing_numbers = range_set - tup_set
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]