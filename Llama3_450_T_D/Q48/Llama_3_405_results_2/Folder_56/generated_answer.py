def return_binary_or_hexa(t):
    a = t[7]
    b = t[9]
    nums = set(range(a + 1, b))
    present_nums = set(t[8:])
    missing_nums = nums - present_nums
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]