def return_binary_or_hexa(tup):
    a = tup[11]
    b = tup[76]
    missing_numbers = set(range(a + 1, b)) - set(tup[11:77])
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 1:
        return format(sum_missing, 'b')
    else:
        return format(sum_missing, 'x')