def return_binary_or_hexa(tup):
    a = tup[70]
    b = tup[98]
    if a + 1 >= b:
        return ''
    missing_nums = set(range(a + 1, b)) - set(tup[70:99])
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]