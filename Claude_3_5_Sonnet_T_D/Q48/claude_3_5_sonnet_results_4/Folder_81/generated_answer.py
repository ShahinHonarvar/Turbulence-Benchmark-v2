def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[100]
    excluded_set = set(tuple_input[10:101])
    sum_value = sum((x for x in range(a + 1, b) if x not in excluded_set))
    if sum_value == 0:
        return ''
    if sum_value % 2 == 1:
        return bin(sum_value)[2:]
    else:
        return hex(sum_value)[2:]