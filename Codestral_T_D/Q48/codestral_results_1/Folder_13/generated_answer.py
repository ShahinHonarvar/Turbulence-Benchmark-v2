def return_binary_or_hexa(tup):
    a = tup[46]
    b = tup[91]
    missing = set(range(a + 1, b)) - set(tup[46:92])
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]