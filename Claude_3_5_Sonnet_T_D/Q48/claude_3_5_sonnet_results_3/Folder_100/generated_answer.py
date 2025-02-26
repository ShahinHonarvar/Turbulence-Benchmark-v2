def return_binary_or_hexa(tuple_input):
    a = tuple_input[44]
    b = tuple_input[78]
    all_numbers = set(range(a + 1, b))
    excluded_numbers = set(tuple_input[44:79])
    missing_numbers = all_numbers - excluded_numbers
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]