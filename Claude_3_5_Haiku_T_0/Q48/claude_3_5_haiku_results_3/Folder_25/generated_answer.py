def return_binary_or_hexa(nums):
    a = nums[37]
    b = nums[43]
    missing_nums = [num for num in range(a + 1, b) if num not in nums[37:44]]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]