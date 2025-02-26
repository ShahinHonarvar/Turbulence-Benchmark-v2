def return_binary_or_hexa(nums):
    a = nums[11]
    b = nums[76]
    full_range = set(range(a + 1, b))
    existing_range = set(nums[11:77])
    missing_nums = full_range - existing_range
    if not missing_nums:
        return ''
    total_sum = sum(missing_nums)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]