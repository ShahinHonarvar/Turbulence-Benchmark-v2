def return_binary_or_hexa(t):
    a = t[86]
    b = t[89]
    missing_numbers = set(range(a + 1, b)) - set(t[86:89])
    sum_missing = sum(missing_numbers)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]