def return_binary_or_hexa(tuple_input):
    a = tuple_input[0]
    b = tuple_input[10]
    set_range = set(range(a + 1, b))
    set_tuple = set(tuple_input[1:10])
    missing_numbers = set_range - set_tuple
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]