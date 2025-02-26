def return_binary_or_hexa(tuple_input):
    a = tuple_input[22]
    b = tuple_input[24]
    sum_range = sum(set(range(a + 1, b)) - set(tuple_input[22:25]))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:].rstrip('L')