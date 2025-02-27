def return_binary_or_hexa(t):
    a, b = (t[0], t[4])
    missing = set(range(a + 1, b)) - set(t[1:5])
    if not missing:
        return ''
    s = sum(missing)
    return format(s, 'b') if s % 2 else format(s, 'x')