def return_binary_or_hexa(tuple_input):
    a = tuple_input[13]
    b = tuple_input[76]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[13:77])
    sum_result = sum(range_set - tuple_set)
    if sum_result == 0:
        return ''
    elif sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].rstrip('L')