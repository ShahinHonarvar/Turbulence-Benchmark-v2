def return_binary_or_hexa(tuple_input):
    a = tuple_input[0]
    b = tuple_input[6]
    excluded_set = set(tuple_input[0:7])
    sum_range = sum((i for i in range(a + 1, b) if i not in excluded_set))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]