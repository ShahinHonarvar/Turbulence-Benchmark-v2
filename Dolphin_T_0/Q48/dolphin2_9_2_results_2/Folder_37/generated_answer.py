def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    total = sum(set(range(a + 1, b)) - set(t[3:7]))
    if total % 2:
        return format(total, 'b')
    else:
        return format(total, 'x')