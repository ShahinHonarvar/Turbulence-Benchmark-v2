def return_binary_or_hexa(tup):
    a = tup[15]
    b = tup[57]
    missing = set(range(a + 1, b)) - set(tup[15:58])
    if missing:
        sum_missing = sum(missing)
        if sum_missing % 2 == 0:
            return hex(sum_missing)[2:]
        else:
            return bin(sum_missing)[2:]
    else:
        return ''