def return_binary_or_hexa(tuple_input):
    a = tuple_input[56]
    b = tuple_input[88]
    missing_nums = set(range(a + 1, b)) - set(tuple_input[56:89])
    sum_nums = sum(missing_nums)
    if sum_nums == 0:
        return ''
    elif sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]