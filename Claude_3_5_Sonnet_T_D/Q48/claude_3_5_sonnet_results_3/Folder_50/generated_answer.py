def return_binary_or_hexa(tuple_input):
    a = tuple_input[13]
    b = tuple_input[76]
    excluded_range = set(tuple_input[13:77])
    sum_value = sum((num for num in range(a + 1, b) if num not in excluded_range))
    if sum_value == 0:
        return ''
    if sum_value % 2 != 0:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]