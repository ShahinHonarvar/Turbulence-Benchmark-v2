def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[8])
    missing_sum = sum(set(range(a + 1, b)) - set(tup[:9]))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')