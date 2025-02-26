def return_binary_or_hexa(tuple_input):
    a = tuple_input[57]
    b = tuple_input[84]
    sum_val = sum(set(range(a + 1, b)) - set(tuple_input[57:85]))
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].lstrip('0')