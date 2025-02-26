def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[100]
    sum_result = sum(set(range(a + 1, b)) - set(tuple_input[10:101]))
    if sum_result == 0:
        return ''
    elif sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]