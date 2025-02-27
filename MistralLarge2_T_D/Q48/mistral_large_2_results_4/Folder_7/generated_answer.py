def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    target_range = set(range(a + 1, b))
    nums_set = set(nums[10:98])
    missing_sum = sum(target_range - nums_set)
    if not missing_sum:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]