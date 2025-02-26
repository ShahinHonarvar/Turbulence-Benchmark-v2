def return_binary_or_hexa(tuple_input):
    a = tuple_input[36]
    b = tuple_input[85]
    sum_result = sum(set(range(a + 1, b)) - set(tuple_input[36:86]))
    if sum_result == 0:
        return ''
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].rstrip('L')