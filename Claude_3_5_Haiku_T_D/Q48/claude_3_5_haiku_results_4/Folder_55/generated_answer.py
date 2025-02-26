def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[12]
    range_set = set(range(a + 1, b))
    tuple_subset = set(tup[10:13])
    missing_nums = range_set - tuple_subset
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]