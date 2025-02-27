def return_binary_or_hexa(tup):
    a, b = (tup[20], tup[51])
    missing = set(range(a + 1, b)) - set(tup[20:52])
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''