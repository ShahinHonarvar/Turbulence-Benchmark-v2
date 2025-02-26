def return_binary_or_hexa(tuple_input):
    a = tuple_input[86]
    b = tuple_input[90]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tuple_input[86:91])
    missing_nums = sum_range - sum_tuple
    total_sum = sum(missing_nums)
    if not total_sum:
        return ''
    elif total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]