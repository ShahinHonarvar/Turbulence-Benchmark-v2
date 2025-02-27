def return_binary_or_hexa(tup):
    a = tup[57]
    b = tup[84]
    sum_missing = sum((x for x in range(a + 1, b) if x not in tup[57:84]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]