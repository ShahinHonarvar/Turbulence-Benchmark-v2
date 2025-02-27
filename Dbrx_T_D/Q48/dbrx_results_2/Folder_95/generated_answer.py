def return_binary_or_hexa(input_tuple):
    a = input_tuple[32]
    b = input_tuple[99]
    present_set = set(input_tuple[33:99])
    missing_numbers = set(range(a + 1, b)) - present_set
    if not missing_numbers:
        return ''
    total = sum(missing_numbers)
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()