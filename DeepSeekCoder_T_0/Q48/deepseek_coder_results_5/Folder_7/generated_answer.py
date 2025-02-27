def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[97]
    missing_integers = set(range(a + 1, b)) - set(tup[10:98])
    sum_missing = sum(missing_integers)
    if sum_missing % 2 == 1:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')