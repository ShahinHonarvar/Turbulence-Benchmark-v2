def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    missing_nums = set(range(a + 1, b))
    present_nums = set(t[20 + 1:43])
    missing_in_range = missing_nums - present_nums
    sum_missing = sum(missing_in_range)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''