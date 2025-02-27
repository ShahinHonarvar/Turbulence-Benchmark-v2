def return_binary_or_hexa(tup):
    a, b = (tup[56], tup[88])
    present = set(tup[56:89])
    missing = set(range(a + 1, b)) - present
    if not missing:
        return ''
    sum_val = sum(missing)
    if sum_val % 2:
        return format(sum_val, 'b')
    else:
        return format(sum_val, 'x')