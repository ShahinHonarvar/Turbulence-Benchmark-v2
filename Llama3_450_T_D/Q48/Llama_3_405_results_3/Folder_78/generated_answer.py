def return_binary_or_hexa(tup):
    a = tup[62]
    b = tup[96]
    actual_nums = set(range(a + 1, b))
    present_nums = set(tup[63:96])
    missing_nums = actual_nums - present_nums
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]