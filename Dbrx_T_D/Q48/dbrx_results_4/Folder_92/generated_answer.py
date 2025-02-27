def return_binary_or_hexa(input_tuple):
    a, _, b = input_tuple
    present_numbers = set(range(a + 1, b))
    all_numbers = set(range(a + 1, b + 1))
    missing_numbers = all_numbers - present_numbers
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()