def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[67]
    missing_nums = set(range(a + 1, b)) - set(tup[44 + 1:67])
    s = sum(missing_nums)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''