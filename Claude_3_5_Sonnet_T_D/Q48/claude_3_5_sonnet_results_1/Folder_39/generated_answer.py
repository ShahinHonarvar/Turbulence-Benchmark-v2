def return_binary_or_hexa(tuple_input):
    a = tuple_input[44]
    b = tuple_input[91]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tuple_input[44:92])
    missing_nums = sum_range - sum_tuple
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]