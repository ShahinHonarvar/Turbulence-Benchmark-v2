def return_binary_or_hexa(t):
    a, b = (t[0], t[2])
    missing_nums = [x for x in range(a + 1, b) if x not in t]
    if missing_nums:
        sum_missing_nums = sum(missing_nums)
        if sum_missing_nums % 2 != 0:
            return bin(sum_missing_nums)[2:]
        else:
            return hex(sum_missing_nums)[2:]
    else:
        return ''