def return_binary_or_hexa(tuple_input):
    a = tuple_input[17]
    b = tuple_input[88]
    set_range = set(range(a + 1, b))
    set_tuple = set(tuple_input[17:89])
    sum_result = sum(set_range - set_tuple)
    if sum_result == 0:
        return ''
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]