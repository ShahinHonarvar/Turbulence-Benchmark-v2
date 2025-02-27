def return_binary_or_hexa(input_tuple):
    a = input_tuple[110]
    b = input_tuple[348]
    present_numbers = set(input_tuple[110:349])
    missing_numbers = set(range(a + 1, b))
    missing_numbers.difference_update(present_numbers)
    total_sum = sum(missing_numbers)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].upper()