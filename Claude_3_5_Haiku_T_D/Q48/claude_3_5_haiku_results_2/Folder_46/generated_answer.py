def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[79]
    missing_nums = set(range(a + 1, b)) - set(tup[10:80])
    if not missing_nums:
        return ''
    sum_missing = sum(missing_nums)
    return bin(sum_missing)[2:] if sum_missing % 2 else hex(sum_missing)[2:]