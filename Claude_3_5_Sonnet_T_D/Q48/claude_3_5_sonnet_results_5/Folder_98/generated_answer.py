def return_binary_or_hexa(tuple_input):
    a = tuple_input[6]
    b = tuple_input[7]
    sum_range = sum(set(range(a + 1, b)) - set(tuple_input[6:8]))
    if sum_range == 0:
        return ''
    elif sum_range % 2 == 1:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:].rstrip('L')