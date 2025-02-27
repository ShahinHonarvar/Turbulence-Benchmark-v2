def return_binary_or_hexa(t):
    a = t[1]
    b = t[7]
    s = set(range(a + 1, b))
    missing_nums = s - set(t[1:8])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]