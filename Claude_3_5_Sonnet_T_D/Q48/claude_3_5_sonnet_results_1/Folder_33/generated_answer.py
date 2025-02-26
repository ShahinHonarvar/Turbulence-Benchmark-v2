def return_binary_or_hexa(tuple_input):
    a = tuple_input[13]
    b = tuple_input[35]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tuple_input[14:35])
    missing_sum = sum(sum_range - sum_tuple)
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]