def return_binary_or_hexa(tup):
    a = tup[39]
    b = tup[43]
    missing_numbers = set(range(a + 1, b)) - set(tup[39:44])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')