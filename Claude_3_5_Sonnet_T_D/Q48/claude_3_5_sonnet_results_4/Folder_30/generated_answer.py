def return_binary_or_hexa(tuple_input):
    a = tuple_input[22]
    b = tuple_input[24]
    sum_missing = sum(set(range(a + 1, b)) - set(tuple_input[22:25]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()