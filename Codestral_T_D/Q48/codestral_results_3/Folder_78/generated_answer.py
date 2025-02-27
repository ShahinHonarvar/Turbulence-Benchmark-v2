def return_binary_or_hexa(tup):
    a = tup[62]
    b = tup[96]
    missing = set(range(a + 1, b)) - set(tup[62:96])
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing != 0:
        return hex(sum_missing)[2:]
    else:
        return ''