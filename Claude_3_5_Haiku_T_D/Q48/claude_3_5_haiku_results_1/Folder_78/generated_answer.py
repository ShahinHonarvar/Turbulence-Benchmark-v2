def return_binary_or_hexa(nums):
    a = nums[62]
    b = nums[96]
    missing_nums = []
    for num in range(a + 1, b):
        if num not in nums[62:97]:
            missing_nums.append(num)
    if not missing_nums:
        return ''
    missing_sum = sum(missing_nums)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]