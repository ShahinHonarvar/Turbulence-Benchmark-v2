def return_binary_or_hexa(tup):
    a = tup[110]
    b = tup[348]
    sum_missing = sum((i for i in range(a + 1, b) if i not in tup[110:349]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]