def return_binary_or_hexa(t):
    a = t[20]
    b = t[35]
    missing_nums = [x for x in range(a + 1, b) if x not in t[20:36]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]