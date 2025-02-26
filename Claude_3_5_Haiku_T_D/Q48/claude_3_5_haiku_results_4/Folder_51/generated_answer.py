def return_binary_or_hexa(nums):
    a = nums[6]
    b = nums[9]
    missing_nums = [num for num in range(a + 1, b) if num not in nums[6:10]]
    total_sum = sum(missing_nums)
    if not missing_nums:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]