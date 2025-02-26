def return_binary_or_hexa(tuple_input):
    a = tuple_input[18]
    b = tuple_input[60]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[18:61])
    missing_nums = range_set - tuple_set
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')