def return_binary_or_hexa(t):
    a = t[38]
    b = t[52]
    missing_nums = [n for n in range(a + 1, b) if n not in t[38:53]]
    if not missing_nums:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]