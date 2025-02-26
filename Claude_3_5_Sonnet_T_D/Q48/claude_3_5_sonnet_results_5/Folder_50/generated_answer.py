def return_binary_or_hexa(tuple_input):
    a = tuple_input[13]
    b = tuple_input[76]
    set_range = set(range(a + 1, b))
    set_tuple = set(tuple_input[13:77])
    sum_not_present = sum(set_range - set_tuple)
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:]