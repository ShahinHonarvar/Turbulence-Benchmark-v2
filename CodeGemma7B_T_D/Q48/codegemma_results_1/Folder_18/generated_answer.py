def return_binary_or_hexa(t):
    n = t[90] - t[56] - 1
    s = sum(set(range(t[56] + 1, t[90])) - set(t[56:90]))
    if s % 2:
        return format(s, 'b')
    else:
        return format(s, 'x').upper()