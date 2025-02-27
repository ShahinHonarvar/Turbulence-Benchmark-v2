def return_binary_or_hexa(tup):
    a = tup[56]
    b = tup[90]
    expected_nums = set(range(a + 1, b))
    actual_nums = set(tup[57:90])
    missing_nums = expected_nums - actual_nums
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]