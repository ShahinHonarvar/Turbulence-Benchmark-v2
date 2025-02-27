def return_binary_or_hexa(tup):
    a, b = (tup[0], tup[5])
    full_set = set(range(a + 1, b))
    tup_set = set(tup[1:5])
    missing_nums = full_set - tup_set
    total = sum(missing_nums)
    if not total:
        return ''
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]