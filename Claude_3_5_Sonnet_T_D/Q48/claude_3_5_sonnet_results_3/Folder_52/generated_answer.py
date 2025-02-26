def return_binary_or_hexa(tuple_input):
    a = tuple_input[38]
    b = tuple_input[81]
    range_set = set(range(a + 1, b))
    tuple_set = set(tuple_input[38:82])
    missing_nums = range_set - tuple_set
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].rstrip('L')