def return_binary_or_hexa(tuple_input):
    a = tuple_input[20]
    b = tuple_input[200]
    tuple_range = set(tuple_input[20:201])
    sum_value = sum((num for num in range(a + 1, b) if num not in tuple_range))
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].rstrip('L')