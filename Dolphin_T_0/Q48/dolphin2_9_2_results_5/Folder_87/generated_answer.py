def return_binary_or_hexa(t):
    a = t[20]
    b = t[43]
    missing_nums = [num for num in range(a + 1, b) if num not in t[20:44]]
    if len(missing_nums) != 0:
        sum_missing_nums = sum(missing_nums)
        if sum_missing_nums % 2 == 0:
            return hex(sum_missing_nums)[2:]
        else:
            return bin(sum_missing_nums)[2:]
    else:
        return ''