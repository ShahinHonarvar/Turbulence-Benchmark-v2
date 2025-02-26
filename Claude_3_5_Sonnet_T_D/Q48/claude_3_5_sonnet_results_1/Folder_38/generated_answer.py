def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[85]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(tup[37:85])
    missing_nums = sum_range - sum_tuple
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]