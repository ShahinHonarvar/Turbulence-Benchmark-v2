def return_binary_or_hexa(tup):
    a, b = (tup[50], tup[200])
    present_nums = set(tup[50:201])
    missing_nums = set(range(a + 1, b)) - present_nums
    if not missing_nums:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()