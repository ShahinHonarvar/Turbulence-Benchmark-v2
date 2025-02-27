def return_binary_or_hexa(tup):
    a = tup[19]
    b = tup[32]
    missing_numbers = set(range(a + 1, b)) - set(tup[19:33])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')