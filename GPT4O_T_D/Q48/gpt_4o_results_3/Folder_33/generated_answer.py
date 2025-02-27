def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[35]
    in_range_set = set(nums[14:35])
    missing_sum = sum((x for x in range(a + 1, b) if x not in in_range_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]