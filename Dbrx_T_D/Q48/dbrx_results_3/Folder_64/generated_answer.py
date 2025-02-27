def return_binary_or_hexa(t):
    a, b = (t[0], t[5])
    sum_of_missing = 0
    missing = set(range(a + 1, b))
    present = set(t[1:5])
    missing -= present
    if not missing:
        return ''
    sum_of_missing = sum(missing)
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return hex(sum_of_missing)