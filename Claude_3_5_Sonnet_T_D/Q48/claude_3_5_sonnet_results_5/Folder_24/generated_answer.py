def return_binary_or_hexa(tuple_input):
    a = tuple_input[13]
    b = tuple_input[91]
    set_in_tuple = set(tuple_input[13:92])
    sum_not_in_tuple = sum((num for num in range(a + 1, b) if num not in set_in_tuple))
    if sum_not_in_tuple == 0:
        return ''
    if sum_not_in_tuple % 2 == 1:
        return bin(sum_not_in_tuple)[2:]
    else:
        return hex(sum_not_in_tuple)[2:]