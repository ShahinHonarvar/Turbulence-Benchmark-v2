def return_binary_or_hexa(int_tuple):
    a = int_tuple[13]
    b = int_tuple[70]
    present_numbers = set(int_tuple[13:71])
    missing_numbers = set(range(a + 1, b)) - present_numbers
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    if sum_of_missing_numbers % 2:
        return bin(sum_of_missing_numbers)[2:]
    else:
        return hex(sum_of_missing_numbers)[2:].upper()