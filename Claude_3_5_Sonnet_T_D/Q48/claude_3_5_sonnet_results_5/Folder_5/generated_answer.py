def return_binary_or_hexa(tuple_input):
    a = tuple_input[2]
    b = tuple_input[8]
    sum_not_in_tuple = sum(set(range(a + 1, b)) - set(tuple_input[2:9]))
    if sum_not_in_tuple == 0:
        return ''
    elif sum_not_in_tuple % 2 != 0:
        return bin(sum_not_in_tuple)[2:]
    else:
        return hex(sum_not_in_tuple)[2:].lstrip('0')