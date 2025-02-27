def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[9])
    missing_sum = sum(set(range(a + 1, b)) - set(tup[:10]))
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')