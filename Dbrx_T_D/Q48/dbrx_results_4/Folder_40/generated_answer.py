def return_binary_or_hexa(t):
    a, b = (t[0], t[3])
    present = set(t[1:4])
    missing = set(range(a + 1, b)) - present
    if not missing:
        return ''
    s = sum(missing)
    if s % 2:
        return format(s, 'b')
    else:
        return format(s, 'x')