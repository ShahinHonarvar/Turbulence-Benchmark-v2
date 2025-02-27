def return_binary_or_hexa(t):
    a = t[10]
    b = t[76]
    expected = set(range(a + 1, b))
    actual = set(t[11:76])
    missing = expected - actual
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]