def return_binary_or_hexa(tup):
    a, b = (tup[57], tup[85])
    nums_in_range = set(tup[57:86])
    all_nums_in_range = set(range(a + 1, b))
    missing_nums = sorted(list(all_nums_in_range - nums_in_range))
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]