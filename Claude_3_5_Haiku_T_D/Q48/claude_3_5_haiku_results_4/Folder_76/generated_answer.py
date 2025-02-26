def return_binary_or_hexa(t):
    a = t[450]
    b = t[905]
    missing_nums = set(range(a + 1, b))
    for num in t[450:906]:
        if num in missing_nums:
            missing_nums.remove(num)
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]