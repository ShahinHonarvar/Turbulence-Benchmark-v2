def return_binary_or_hexa(tuple_input):
    a = tuple_input[6]
    b = tuple_input[7]
    excluded_set = set(tuple_input[6:8])
    sum_excluded = sum((x for x in range(a + 1, b) if x not in excluded_set))
    if sum_excluded == 0:
        return ''
    elif sum_excluded % 2 == 1:
        return bin(sum_excluded)[2:]
    else:
        return hex(sum_excluded)[2:]