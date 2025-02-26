def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[12]
    sum_of_missing = sum(set(range(a + 1, b)) - set(tuple_input[10:13]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]