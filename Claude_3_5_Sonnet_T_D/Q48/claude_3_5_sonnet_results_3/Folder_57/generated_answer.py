def return_binary_or_hexa(tuple_input):
    a = tuple_input[25]
    b = tuple_input[80]
    sum_value = sum(set(range(a + 1, b)) - set(tuple_input[25:81]))
    if sum_value == 0:
        return ''
    elif sum_value % 2 != 0:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]