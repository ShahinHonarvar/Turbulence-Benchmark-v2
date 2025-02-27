def return_binary_or_hexa(tup):
    a = tup[90]
    b = tup[200]
    missing = set(range(a + 1, b)) - set(tup[90:201])
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')