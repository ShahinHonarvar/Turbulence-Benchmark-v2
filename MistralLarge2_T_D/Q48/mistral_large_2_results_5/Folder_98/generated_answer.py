def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    missing_nums = set(range(a + 1, b)) - set(t[6:8])
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]