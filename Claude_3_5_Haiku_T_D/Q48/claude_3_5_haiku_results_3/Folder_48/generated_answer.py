def return_binary_or_hexa(nums):
    a = nums[933]
    b = nums[996]
    missing_nums = [x for x in range(a + 1, b) if x not in nums[933:997]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]