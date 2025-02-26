def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[70]
    missing_nums = set(range(a + 1, b))
    for x in nums[13:71]:
        if x in missing_nums:
            missing_nums.remove(x)
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]