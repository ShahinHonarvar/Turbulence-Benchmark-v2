def return_binary_or_hexa(t):
    a = t[51]
    b = t[76]
    expected_nums = set(range(a + 1, b))
    actual_nums = set(t[52:76])
    missing_nums = expected_nums - actual_nums
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]