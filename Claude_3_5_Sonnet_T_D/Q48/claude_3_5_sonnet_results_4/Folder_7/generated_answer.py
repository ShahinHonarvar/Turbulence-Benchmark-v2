def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[97]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tuple_input[10:98])
    missing_nums = sum_range - sum_tuple
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]