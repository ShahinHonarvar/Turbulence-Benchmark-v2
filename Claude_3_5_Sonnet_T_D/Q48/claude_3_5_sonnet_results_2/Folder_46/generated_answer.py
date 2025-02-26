def return_binary_or_hexa(tuple_input):
    a = tuple_input[10]
    b = tuple_input[79]
    set_range = set(range(a + 1, b))
    set_tuple = set(tuple_input[10:80])
    missing_nums = set_range - set_tuple
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]