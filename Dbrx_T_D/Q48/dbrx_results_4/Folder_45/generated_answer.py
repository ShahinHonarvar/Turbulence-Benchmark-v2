def return_binary_or_hexa(input_tuple):
    a = input_tuple[30]
    b = input_tuple[200]
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(input_tuple[30:201])
    missing_numbers -= present_numbers
    if not missing_numbers:
        return ''
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()