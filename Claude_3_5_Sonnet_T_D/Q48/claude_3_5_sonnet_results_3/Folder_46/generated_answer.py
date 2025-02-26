def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[79]
    tuple_range = set(tuple_input[10:80])
    sum_value = sum((num for num in range(a + 1, b) if num not in tuple_range))
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]