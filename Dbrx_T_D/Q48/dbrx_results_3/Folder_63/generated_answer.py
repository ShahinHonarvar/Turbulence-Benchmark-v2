def return_binary_or_hexa(tup):
    a, b = (tup[81], tup[86])
    missing_sum = sum(set(range(a + 1, b)) - set(tup[81:87]))
    if missing_sum % 2:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')