def return_binary_or_hexa(tupl):
    a = tupl[86]
    b = tupl[90]
    missing = set(range(a + 1, b)) - set(tupl[86:90])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''