def return_binary_or_hexa(t):
    if len(t) <= 98:
        return ''
    a, b = (t[70], t[98])
    sum_missing = sum((i for i in range(a + 1, b) if i not in t[71:99]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 0:
        return format(sum_missing, 'x')
    else:
        return format(sum_missing, 'b')