def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[4])
    sum_missing = sum(set(range(a + 1, b)) - set(tup[:5]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]