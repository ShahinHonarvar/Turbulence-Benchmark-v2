def return_binary_or_hexa(tup):
    a = tup[69]
    b = tup[97]
    range_set = set(range(a + 1, b))
    tuple_set = set(tup[69:98])
    missing_numbers = range_set - tuple_set
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')