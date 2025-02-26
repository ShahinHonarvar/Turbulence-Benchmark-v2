def return_binary_or_hexa(tuple_input):
    a = tuple_input[57]
    b = tuple_input[84]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tuple_input[57:85])
    sum_diff = sum(sum_range - sum_tuple)
    if sum_diff == 0:
        return ''
    elif sum_diff % 2 == 1:
        return bin(sum_diff)[2:]
    else:
        return hex(sum_diff)[2:].rstrip('L')