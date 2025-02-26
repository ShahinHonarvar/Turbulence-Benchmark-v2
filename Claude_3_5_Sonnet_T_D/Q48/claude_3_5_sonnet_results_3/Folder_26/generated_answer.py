def return_binary_or_hexa(tuple_input):
    a = tuple_input[68]
    b = tuple_input[99]
    sum_missing = sum(set(range(a + 1, b)) - set(tuple_input[68:100]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()