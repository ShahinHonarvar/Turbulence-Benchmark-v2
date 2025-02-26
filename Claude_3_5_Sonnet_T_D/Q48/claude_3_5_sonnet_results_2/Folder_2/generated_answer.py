def return_binary_or_hexa(tuple_input):
    a = tuple_input[72]
    b = tuple_input[93]
    excluded_numbers = set(tuple_input[72:94])
    sum_value = sum((num for num in range(a + 1, b) if num not in excluded_numbers))
    if sum_value == 0:
        return ''
    elif sum_value % 2 != 0:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].rstrip('L')