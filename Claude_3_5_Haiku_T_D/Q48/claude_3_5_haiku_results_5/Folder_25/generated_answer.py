def return_binary_or_hexa(input_tuple):
    a = input_tuple[37]
    b = input_tuple[43]
    missing_numbers = set(range(a + 1, b)) - set(input_tuple[37:44])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]