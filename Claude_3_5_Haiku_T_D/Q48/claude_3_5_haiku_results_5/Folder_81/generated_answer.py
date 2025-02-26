def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[100]
    missing_nums = set(range(a + 1, b))
    for num in nums[11:100]:
        if num in missing_nums:
            missing_nums.remove(num)
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]