def return_binary_or_hexa(tuple_input):
    a = tuple_input[57]
    b = tuple_input[85]
    excluded_set = set(tuple_input[57:86])
    sum_value = sum((num for num in range(a + 1, b) if num not in excluded_set))
    if sum_value == 0:
        return ''
    if sum_value % 2 != 0:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].rstrip('L')