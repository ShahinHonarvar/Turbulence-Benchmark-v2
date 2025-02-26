def return_binary_or_hexa(tuple_input):
    a = tuple_input[56]
    b = tuple_input[90]
    all_numbers = set(range(a + 1, b))
    numbers_in_tuple = set(tuple_input[57:90])
    missing_numbers = all_numbers - numbers_in_tuple
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]