def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[35]
    range_set = set(range(a + 1, b))
    tup_set = set(tup[13:36])
    missing_numbers = range_set - tup_set
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')