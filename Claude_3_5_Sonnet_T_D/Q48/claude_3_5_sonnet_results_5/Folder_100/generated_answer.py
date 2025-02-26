def return_binary_or_hexa(tuple_input):
    a = tuple_input[44]
    b = tuple_input[78]
    set_range = set(range(a + 1, b))
    set_tuple = set(tuple_input[44:79])
    sum_missing = sum(set_range - set_tuple)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]