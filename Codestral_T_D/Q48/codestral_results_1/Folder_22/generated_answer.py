def return_binary_or_hexa(tup):
    a, b = (tup[40], tup[200])
    missing = set(range(a + 1, b)) - set(tup[41:200])
    sum_missing = sum(missing)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]