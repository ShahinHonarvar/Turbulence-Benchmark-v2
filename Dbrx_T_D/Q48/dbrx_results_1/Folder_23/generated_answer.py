def return_binary_or_hexa(int_tuple):
    a = int_tuple[20]
    b = int_tuple[36]
    missing_numbers = set(range(a + 1, b)) - set(int_tuple[20:37])
    if not missing_numbers:
        return ''
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()