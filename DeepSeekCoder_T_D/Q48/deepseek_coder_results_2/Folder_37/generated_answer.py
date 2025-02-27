def return_binary_or_hexa(tup):
    a = tup[2]
    b = tup[7]
    missing_integers = set(range(a + 1, b)) - set(tup[2:8])
    if not missing_integers:
        return ''
    sum_missing = sum(missing_integers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]