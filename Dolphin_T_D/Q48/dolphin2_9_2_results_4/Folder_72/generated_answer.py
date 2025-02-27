def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    range_nums = list(range(a + 1, b))
    missing_nums = [i for i in range_nums if i not in t]
    sum_of_missing = sum(missing_nums)
    if len(missing_nums) == 0:
        return ''
    elif sum_of_missing % 2 == 0:
        return hex(sum_of_missing)[2:]
    else:
        return bin(sum_of_missing)[2:]