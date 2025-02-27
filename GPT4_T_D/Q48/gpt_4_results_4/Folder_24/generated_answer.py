def return_binary_or_hexa(tup):
    a = tup[13]
    b = tup[91]
    missing_nums = set(range(a + 1, b)) - set(tup[14:91])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 != 0:
        return format(sum_missing_nums, 'b')
    else:
        return format(sum_missing_nums, 'x')