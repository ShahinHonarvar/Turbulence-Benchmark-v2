def return_binary_or_hexa(t):
    a = t[38]
    b = t[81]
    nums = set(range(a + 1, b))
    present_nums = set(t[39:81])
    sum_missing_nums = sum(nums - present_nums)
    if sum_missing_nums == 0:
        return ''
    elif sum_missing_nums % 2 != 0:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:]