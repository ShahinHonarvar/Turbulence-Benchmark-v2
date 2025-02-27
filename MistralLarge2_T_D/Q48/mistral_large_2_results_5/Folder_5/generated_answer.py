def return_binary_or_hexa(tup):
    a, b = (tup[2], tup[8])
    integers_between = set(range(a + 1, b))
    missing_integers = integers_between - set(tup[2:9])
    if not missing_integers:
        return ''
    sum_missing = sum(missing_integers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]