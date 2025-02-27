def return_binary_or_hexa(t):
    a = t[60]
    b = t[90]
    missing_nums = set(range(a + 1, b)) - set(t[61:90])
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''