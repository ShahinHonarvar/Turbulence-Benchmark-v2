def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[30:201]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]