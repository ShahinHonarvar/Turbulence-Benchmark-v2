def return_binary_or_hexa(tup):
    a, b = (tup[86], tup[90])
    present = set(tup[86:91])
    missing = set(range(a + 1, b))
    missing -= present
    if not missing:
        return ''
    sum_val = sum(missing)
    if sum_val % 2:
        return format(sum_val, 'b')
    else:
        return hex(sum_val)