def return_binary_or_hexa(input_tuple):
    a, b = (input_tuple[0], input_tuple[4])
    missing_numbers = [num for num in range(a + 1, b) if num not in input_tuple[:5]]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]