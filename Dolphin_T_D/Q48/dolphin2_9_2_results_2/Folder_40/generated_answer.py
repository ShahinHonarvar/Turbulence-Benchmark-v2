def return_binary_or_hexa(t):
    a, _, _, b = t
    missing_nums = set(range(a + 1, b)) - set(t)
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]