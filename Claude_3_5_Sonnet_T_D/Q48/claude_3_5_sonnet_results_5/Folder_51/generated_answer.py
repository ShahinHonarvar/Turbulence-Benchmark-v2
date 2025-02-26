def return_binary_or_hexa(tuple_input):
    a = tuple_input[6]
    b = tuple_input[9]
    excluded_set = set(tuple_input[6:10])
    sum_result = sum((num for num in range(a + 1, b) if num not in excluded_set))
    if sum_result == 0:
        return ''
    if sum_result % 2 != 0:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]