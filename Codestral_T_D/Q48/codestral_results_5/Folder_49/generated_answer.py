def return_binary_or_hexa(tupl):
    a = tupl[80]
    b = tupl[200]
    missing_nums = set(range(a + 1, b)) - set(tupl[81:200])
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]