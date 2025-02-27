def return_binary_or_hexa(t):
    if t[74] <= t[83]:
        return ''
    s = 0
    for i in range(t[74] + 1, t[84]):
        if i not in t[73:84]:
            s += i
    return format(s, 'b') if s % 2 else format(s, 'x')