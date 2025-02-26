def return_binary_or_hexa(tuple_input):
    a = tuple_input[45]
    b = tuple_input[48]
    missing_numbers = [num for num in range(a + 1, b) if num not in tuple_input[45:49]]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]