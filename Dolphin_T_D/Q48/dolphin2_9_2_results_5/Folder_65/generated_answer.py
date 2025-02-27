def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    missing_nums = [x for x in range(a + 1, b) if x not in t]
    if len(missing_nums) == 0:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]