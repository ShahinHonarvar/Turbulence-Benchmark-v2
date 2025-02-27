def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[79]
    range_set = set(range(a + 1, b))
    tuple_set = set(tup[11:80])
    missing_numbers = range_set - tuple_set
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]