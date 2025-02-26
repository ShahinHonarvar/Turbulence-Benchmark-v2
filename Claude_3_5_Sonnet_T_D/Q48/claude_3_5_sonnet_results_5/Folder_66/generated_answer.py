def return_binary_or_hexa(t):
    a = t[11]
    b = t[76]
    range_set = set(range(a + 1, b))
    tuple_set = set(t[11:77])
    missing_nums = range_set - tuple_set
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]