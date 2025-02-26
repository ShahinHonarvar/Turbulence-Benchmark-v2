def return_binary_or_hexa(tuple_input):
    a = tuple_input[32]
    b = tuple_input[99]
    all_numbers = set(range(a + 1, b))
    present_numbers = set(tuple_input[32:100])
    missing_numbers = all_numbers - present_numbers
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]