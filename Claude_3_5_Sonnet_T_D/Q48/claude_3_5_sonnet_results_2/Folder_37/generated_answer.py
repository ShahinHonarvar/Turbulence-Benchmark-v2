def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    sum_range = set(range(a + 1, b))
    sum_tuple = set(t[2:8])
    missing_nums = sum_range - sum_tuple
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]