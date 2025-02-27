def return_binary_or_hexa(t):
    a = t[27]
    b = t[96]
    missing_nums = []
    for i in range(a + 1, b):
        if i not in t:
            missing_nums.append(i)
    if len(missing_nums) == 0:
        return ''
    _sum = sum(missing_nums)
    if _sum % 2 == 0:
        return hex(_sum)[2:]
    else:
        return bin(_sum)[2:]