def return_binary_or_hexa(input_tuple):
    a = input_tuple[1]
    b = input_tuple[8]
    present_numbers = set(input_tuple[1:9])
    all_numbers = set(range(a + 1, b))
    missing_numbers = all_numbers - present_numbers
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()