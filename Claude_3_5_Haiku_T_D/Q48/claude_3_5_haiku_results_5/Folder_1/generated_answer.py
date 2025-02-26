def return_binary_or_hexa(nums):
    a = nums[17]
    b = nums[88]
    missing_nums = set(range(a + 1, b))
    for num in nums[17:89]:
        if num in missing_nums:
            missing_nums.remove(num)
    total_sum = sum(missing_nums)
    if not missing_nums:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]