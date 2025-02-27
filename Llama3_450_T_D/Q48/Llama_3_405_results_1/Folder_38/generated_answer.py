def return_binary_or_hexa(tup):
    a = tup[36]
    b = tup[85]
    full_set = set(range(a + 1, b))
    tup_set = set(tup[37:85])
    missing_nums = full_set - tup_set
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]