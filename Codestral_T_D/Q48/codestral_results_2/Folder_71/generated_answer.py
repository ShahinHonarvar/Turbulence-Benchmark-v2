def return_binary_or_hexa(t):
    a, b = (t[20], t[35])
    missing_nums = set(range(a + 1, b)) - set(t[20:36])
    s = sum(missing_nums)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''