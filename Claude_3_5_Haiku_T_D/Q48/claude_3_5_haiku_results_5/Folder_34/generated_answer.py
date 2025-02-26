def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[200]
    missing_sum = 0
    for num in range(a + 1, b):
        if num not in nums[60:201]:
            missing_sum += num
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    else:
        return ''