def return_binary_or_hexa(t):
    a = t[36]
    b = t[52]
    missing_nums = set(range(a + 1, b)) - set(t[36:53])
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''