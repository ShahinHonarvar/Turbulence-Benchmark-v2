def return_binary_or_hexa(tuple_in):
    a = tuple_in[39]
    b = tuple_in[43]
    sum_to_return = 0
    for i in range(a + 1, b):
        if i not in tuple_in[39:44]:
            sum_to_return += i
    if sum_to_return == 0:
        return ''
    elif sum_to_return % 2 == 1:
        return bin(sum_to_return)[2:]
    else:
        return hex(sum_to_return)[2:]