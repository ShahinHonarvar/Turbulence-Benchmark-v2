def return_binary_or_hexa(t):
    a, b = (t[50], t[92])
    present = set(t[50:93])
    missing = set(range(a + 1, b)) - present
    if not missing:
        return ''
    total = sum(missing)
    if total % 2:
        return format(total, 'b')
    else:
        return format(total, 'x')