def return_binary_or_hexa(tup):
    a, b = (tup[1], tup[4])
    missing = [x for x in range(a + 1, b) if x not in tup[1:5]]
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]