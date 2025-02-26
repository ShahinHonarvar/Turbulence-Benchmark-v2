def return_binary_or_hexa(tuple_input):
    a = tuple_input[933]
    b = tuple_input[996]
    set_range = set(tuple_input[933:997])
    sum_result = sum((num for num in range(a + 1, b) if num not in set_range))
    if sum_result == 0:
        return ''
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]