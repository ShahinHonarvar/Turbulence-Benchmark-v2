def return_binary_or_hexa(nums):
    if len(nums) < 49:
        return ''
    a = nums[45]
    b = nums[48]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[46:48]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')