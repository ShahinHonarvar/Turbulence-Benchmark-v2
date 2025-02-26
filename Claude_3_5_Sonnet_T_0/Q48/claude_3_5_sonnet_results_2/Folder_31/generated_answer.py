def return_binary_or_hexa(tuple_input):
    a = tuple_input[33]
    b = tuple_input[78]
    excluded_set = set(tuple_input[33:79])
    sum_result = sum((num for num in range(a + 1, b) if num not in excluded_set))
    if sum_result == 0:
        return ''
    if sum_result % 2 == 1:
        return bin(sum_result)[2:]
    else:
        return hex(sum_result)[2:]