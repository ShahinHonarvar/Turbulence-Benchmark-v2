def return_binary_or_hexa(ppr):
    a, b = (ppr[70], ppr[200])
    missing_nums = set(range(a + 1, b)) - set(ppr[70:201])
    sum_missing = sum(missing_nums)
    if sum_missing % 2:
        return bin(sum_missing)[2:]
    return hex(sum_missing)[2:].lower()