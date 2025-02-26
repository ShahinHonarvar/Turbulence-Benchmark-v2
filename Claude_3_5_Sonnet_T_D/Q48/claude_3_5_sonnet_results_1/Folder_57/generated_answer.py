def return_binary_or_hexa(tuple_input):
    a = tuple_input[25]
    b = tuple_input[80]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[25:81])
    missing_numbers = range_set - tuple_set
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]