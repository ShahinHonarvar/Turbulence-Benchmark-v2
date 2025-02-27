def return_binary_or_hexa(tuple_input):
    a = tuple_input[57]
    b = tuple_input[85]
    sum_range = sum((i for i in range(a + 1, b) if i not in tuple_input[57:86]))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]