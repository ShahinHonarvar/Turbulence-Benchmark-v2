def return_binary_or_hexa(input_tuple):
    a = input_tuple[18]
    b = input_tuple[60]
    missing_nums = set(range(a + 1, b))
    tuple_subset = set(input_tuple[18:61])
    missing_nums -= tuple_subset
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]