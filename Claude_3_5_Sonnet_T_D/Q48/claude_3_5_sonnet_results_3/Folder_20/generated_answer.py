def return_binary_or_hexa(tuple_input):
    a = tuple_input[27]
    b = tuple_input[96]
    excluded_set = set(tuple_input[27:97])
    sum_value = sum((num for num in range(a + 1, b) if num not in excluded_set))
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]