def return_binary_or_hexa(tup):
    a = tup[25]
    b = tup[80]
    missing_nums = set(range(a + 1, b)) - set(tup[25:81])
    sum_missing = sum(missing_nums)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ''