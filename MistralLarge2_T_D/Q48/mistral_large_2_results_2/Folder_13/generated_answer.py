def return_binary_or_hexa(tup):
    a = tup[46]
    b = tup[91]
    range_set = set(tup[46:92])
    sum_missing = sum((x for x in range(a + 1, b) if x not in range_set))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]