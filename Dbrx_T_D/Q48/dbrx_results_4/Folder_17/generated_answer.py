def return_binary_or_hexa(t):
    a, b = (t[73], t[84])
    missing = set(range(a + 1, b)) - set(t[73:84])
    if not missing:
        return ''
    s = sum(missing)
    return format(s, 'b') if s % 2 else format(s, 'x')