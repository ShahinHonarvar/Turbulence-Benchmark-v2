def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[2])
    missing_nums = [num for num in range(a + 1, b) if num not in nums]
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]