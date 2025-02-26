def return_binary_or_hexa(t):
    a = t[13]
    b = t[76]
    missing_nums = set(range(a + 1, b)) - set(t[13:77])
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]