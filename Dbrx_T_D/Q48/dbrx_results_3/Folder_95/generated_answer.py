def return_binary_or_hexa(input_tuple):
    a = input_tuple[32]
    b = input_tuple[99]
    missing_numbers = set(range(a + 1, b)) - set(input_tuple[33:99])
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()