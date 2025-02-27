def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[90]
    missing_sum = 0
    present_nums = set(nums[86:91])
    for i in range(a + 1, b):
        if i not in present_nums:
            missing_sum += i
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]