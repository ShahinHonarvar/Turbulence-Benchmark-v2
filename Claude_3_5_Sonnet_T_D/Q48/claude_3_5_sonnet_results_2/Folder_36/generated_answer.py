def return_binary_or_hexa(tuple_input):
    a = tuple_input[110]
    b = tuple_input[348]
    tuple_range = set(tuple_input[110:349])
    sum_value = sum((num for num in range(a + 1, b) if num not in tuple_range))
    if sum_value == 0:
        return ''
    elif sum_value % 2 != 0:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]