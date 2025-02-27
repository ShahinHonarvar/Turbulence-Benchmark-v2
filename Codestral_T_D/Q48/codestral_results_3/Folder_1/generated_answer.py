def return_binary_or_hexa(t):
    a = t[17]
    b = t[88]
    missing_nums = set(range(a + 1, b)) - set(t[17:88])
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]