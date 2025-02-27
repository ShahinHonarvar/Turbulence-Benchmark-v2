def return_binary_or_hexa(t):
    a = t[22]
    b = t[24]
    missing_nums = set(range(a + 1, b)) - set(t[23:24])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]