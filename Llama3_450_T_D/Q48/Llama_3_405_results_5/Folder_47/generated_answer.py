def return_binary_or_hexa(t):
    a = t[29]
    b = t[53]
    existing_nums = set(t[30:53])
    total_nums = set(range(a + 1, b))
    missing_nums = total_nums - existing_nums
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]