def return_binary_or_hexa(t):
    a, b = (t[55], t[84])
    present = set(t[55:85])
    missing = set(range(a + 1, b)) - present
    if not missing:
        return ''
    total = sum(missing)
    if total % 2:
        return format(total, 'b')
    else:
        return format(total, 'x')