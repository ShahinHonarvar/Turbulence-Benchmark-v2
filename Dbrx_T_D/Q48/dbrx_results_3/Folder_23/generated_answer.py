def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[20]
    b = integer_tuple[36]
    missing_numbers = set(range(a + 1, b)) - set(integer_tuple[20:37])
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()