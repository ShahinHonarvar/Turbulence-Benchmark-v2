def return_binary_or_hexa(t):
    a, b = (t[6], t[7])
    missing_nums = [x for x in range(a + 1, b) if x not in t[6:8]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]