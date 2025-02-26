def return_binary_or_hexa(tuple_input):
    a = tuple_input[60]
    b = tuple_input[90]
    sum_value = sum(set(range(a + 1, b)) - set(tuple_input[60:91]))
    if sum_value == 0:
        return ''
    if sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].rstrip('L')