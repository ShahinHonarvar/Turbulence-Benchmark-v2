def return_binary_or_hexa(tuple_input):
    a = tuple_input[51]
    b = tuple_input[76]
    excluded_nums = set(tuple_input[51:77])
    sum_result = sum((num for num in range(a + 1, b) if num not in excluded_nums))
    if sum_result == 0:
        return ''
    elif sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]