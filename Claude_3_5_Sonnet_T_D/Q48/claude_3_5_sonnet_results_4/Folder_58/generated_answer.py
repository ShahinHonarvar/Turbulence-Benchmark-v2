def return_binary_or_hexa(tuple_input):
    a = tuple_input[275]
    b = tuple_input[871]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[275:872])
    missing_numbers = range_set - tuple_set
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]