def return_binary_or_hexa(tuple_input):
    a = tuple_input[20]
    b = tuple_input[36]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[20:37])
    sum_not_present = sum(range_set - tuple_set)
    if sum_not_present == 0:
        return ''
    if sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]