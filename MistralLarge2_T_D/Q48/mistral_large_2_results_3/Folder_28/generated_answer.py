def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in nums[86:99]:
            missing_sum += i
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]