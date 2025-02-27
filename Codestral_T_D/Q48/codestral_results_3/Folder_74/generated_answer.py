def return_binary_or_hexa(t):
    a, b = (t[69], t[97])
    missing_nums = set(range(a + 1, b)) - set(t[69 + 1:97])
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''