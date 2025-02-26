def return_binary_or_hexa(sorted_tuple):
    a = sorted_tuple[30]
    b = sorted_tuple[200]
    missing_nums = set(range(a + 1, b))
    tuple_range_set = set(sorted_tuple[30:201])
    missing_nums -= tuple_range_set
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]