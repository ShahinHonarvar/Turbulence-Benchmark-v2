def return_binary_or_hexa(t):
    a, b = (t[56], t[90])
    full_set = set(range(a + 1, b))
    present_set = set(t[57:91])
    missing_nums = full_set - present_set
    s = sum(missing_nums)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s == 0:
        return ''
    else:
        return hex(s)[2:]