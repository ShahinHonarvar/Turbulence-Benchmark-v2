def return_binary_or_hexa(t):
    a, b = (t[18], t[60])
    missing_sum = sum(set(range(a + 1, b)) - set(t[18:61]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'X')