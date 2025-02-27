def return_binary_or_hexa(nums):
    a = nums[45]
    b = nums[48]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[45:49]))
    if missing_sum % 2:
        return format(missing_sum, 'b')
    else:
        return hex(missing_sum)[2:].upper()