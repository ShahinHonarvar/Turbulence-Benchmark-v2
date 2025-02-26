def return_binary_or_hexa(tuple_input):
    a = tuple_input[36]
    b = tuple_input[85]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[36:86])
    sum_missing = sum(range_set - tuple_set)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]