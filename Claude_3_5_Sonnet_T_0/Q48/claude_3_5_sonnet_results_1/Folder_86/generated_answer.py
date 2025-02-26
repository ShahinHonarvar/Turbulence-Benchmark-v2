def return_binary_or_hexa(tuple_input):
    a = tuple_input[19]
    b = tuple_input[32]
    sum_value = sum(set(range(a + 1, b)) - set(tuple_input[19:33]))
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]