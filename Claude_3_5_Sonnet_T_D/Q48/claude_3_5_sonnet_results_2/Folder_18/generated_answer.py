def return_binary_or_hexa(tuple_input):
    a = tuple_input[56]
    b = tuple_input[90]
    excluded_set = set(tuple_input[56:91])
    sum_result = sum((i for i in range(a + 1, b) if i not in excluded_set))
    if sum_result == 0:
        return ''
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:].rstrip('L')