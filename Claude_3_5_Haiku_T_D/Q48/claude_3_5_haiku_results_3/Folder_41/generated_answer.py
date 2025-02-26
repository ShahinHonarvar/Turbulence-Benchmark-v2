def return_binary_or_hexa(input_tuple):
    a = input_tuple[3]
    b = input_tuple[8]
    range_set = set(range(a + 1, b))
    present_set = set(input_tuple[3:9])
    missing_nums = range_set - present_set
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]