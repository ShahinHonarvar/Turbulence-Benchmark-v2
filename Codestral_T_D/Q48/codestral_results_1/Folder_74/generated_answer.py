def return_binary_or_hexa(tup):
    a, b = (tup[69], tup[97])
    missing = [i for i in range(a + 1, b) if i not in tup[69:98]]
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''