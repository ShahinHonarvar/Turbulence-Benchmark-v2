def return_binary_or_hexa(tuple_of_ints):
    a = tuple_of_ints[46]
    b = tuple_of_ints[91]
    ints_between_a_b = set(range(a + 1, b))
    missing_ints = ints_between_a_b.difference(tuple_of_ints[46:92])
    if not missing_ints:
        return ''
    sum_missing_ints = sum(missing_ints)
    if sum_missing_ints % 2 == 0:
        return hex(sum_missing_ints)[2:]
    else:
        return bin(sum_missing_ints)[2:]