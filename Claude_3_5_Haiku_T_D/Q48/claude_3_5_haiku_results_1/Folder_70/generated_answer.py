def return_binary_or_hexa(t):
    a = t[43]
    b = t[70]
    missing_nums = set(range(a + 1, b))
    for num in t[43:71]:
        if num in missing_nums:
            missing_nums.remove(num)
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]