def return_binary_or_hexa(tuple_input):
    a = tuple_input[20]
    b = tuple_input[51]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tuple_input[20:52])
    sum_result = sum(sum_range - sum_tuple)
    if sum_result == 0:
        return ''
    elif sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]