def return_binary_or_hexa(lst):
    a = lst[933]
    b = lst[996]
    missing_nums = set(range(a + 1, b)) - set(lst[933:996 + 1])
    if not missing_nums:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 != 0:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]