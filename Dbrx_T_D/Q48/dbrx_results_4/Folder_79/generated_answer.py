def return_binary_or_hexa(input_tuple):
    if not all((isinstance(i, int) and i >= 0 for i in input_tuple)) or len(input_tuple) != 8:
        raise ValueError('Invalid input. The input should be a tuple of 8 distinct nonnegative integers.')
    a, b = (input_tuple[1], input_tuple[7])
    if a >= b:
        raise ValueError('Invalid input. The integer at index 1 should be less than the integer at index 7.')
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(input_tuple[1:7])
    missing_numbers -= present_numbers
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = sum(missing_numbers)
    binary_rep = bin(sum_of_missing_numbers)[2:]
    hexadecimal_rep = hex(sum_of_missing_numbers)[2:].upper()
    if int(binary_rep, 2) % 2:
        return binary_rep
    else:
        return hexadecimal_rep