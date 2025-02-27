def return_binary_or_hexa(tuple_arg):
    a = tuple_arg[86]
    b = tuple_arg[90]
    missing_nums = set(range(a + 1, b)) - set(tuple_arg[86:90])
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''