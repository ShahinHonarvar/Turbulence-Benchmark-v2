def return_binary_or_hexa(tuple_input):
    a = tuple_input[72]
    b = tuple_input[93]
    set_in_tuple = set(tuple_input[72:94])
    sum_not_in_tuple = sum((i for i in range(a + 1, b) if i not in set_in_tuple))
    if sum_not_in_tuple == 0:
        return ''
    if sum_not_in_tuple % 2 == 1:
        return bin(sum_not_in_tuple)[2:]
    else:
        return hex(sum_not_in_tuple)[2:].upper()