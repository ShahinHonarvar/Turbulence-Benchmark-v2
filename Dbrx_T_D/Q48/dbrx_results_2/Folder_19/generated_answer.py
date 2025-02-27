def return_binary_or_hexa(input_tuple):
    a, _, _, _, b = input_tuple
    missing_numbers = set(range(a + 1, b)) - set(input_tuple[1:b])
    if not missing_numbers:
        return ''
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()