def return_binary_or_hexa(tup):
    a = tup[57]
    b = tup[84]
    present_nums = set(tup[58:84])
    total_nums = set(range(a + 1, b))
    missing_nums = total_nums - present_nums
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]