def return_binary_or_hexa(input_tuple):
    a = input_tuple[18]
    b = input_tuple[60]
    present_numbers = set(input_tuple[18:61])
    missing_numbers = set(range(a + 1, b))
    missing_and_not_present = missing_numbers - present_numbers
    if not missing_and_not_present:
        return ''
    sum_of_missing_numbers = sum(missing_and_not_present)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()