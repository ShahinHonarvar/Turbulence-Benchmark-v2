def return_binary_or_hexa(tup):
    a = tup[110]
    b = tup[348]
    range_set = set(range(a + 1, b))
    tuple_set = set(tup[110:348])
    missing_numbers = range_set - tuple_set
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
    return ''