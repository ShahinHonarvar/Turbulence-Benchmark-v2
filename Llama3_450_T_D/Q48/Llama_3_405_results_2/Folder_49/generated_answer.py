def return_binary_or_hexa(t):
    a = t[80]
    b = t[200]
    s = set(range(a + 1, b))
    missing = s - set(t[81:200])
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return '{:x}'.format(total)
    else:
        return '{:b}'.format(total)