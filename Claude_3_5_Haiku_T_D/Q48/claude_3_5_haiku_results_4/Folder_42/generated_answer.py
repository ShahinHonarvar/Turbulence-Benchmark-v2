def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[60]
    missing_nums = set(range(a + 1, b))
    for num in nums[18:61]:
        if num in missing_nums:
            missing_nums.remove(num)
    if not missing_nums:
        return ''
    missing_sum = sum(missing_nums)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]