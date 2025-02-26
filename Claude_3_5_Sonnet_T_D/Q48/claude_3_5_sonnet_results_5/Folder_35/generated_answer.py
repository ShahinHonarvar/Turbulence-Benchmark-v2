def return_binary_or_hexa(tup):
    a = tup[77]
    b = tup[84]
    range_set = set(range(a + 1, b))
    tuple_set = set(tup[77:85])
    missing_nums = range_set - tuple_set
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]