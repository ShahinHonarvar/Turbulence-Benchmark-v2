def return_binary_or_hexa(tuple_input):
    a = tuple_input[1]
    b = tuple_input[7]
    excluded_set = set(tuple_input[1:8])
    sum_value = sum((x for x in range(a + 1, b) if x not in excluded_set))
    if sum_value == 0:
        return ''
    elif sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:].rstrip('L')