def return_binary_or_hexa(t):
    a = t[60]
    b = t[90]
    expected = set(range(a + 1, b))
    actual = set(t[61:90])
    missing = expected - actual
    total = sum(missing)
    if not missing:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]