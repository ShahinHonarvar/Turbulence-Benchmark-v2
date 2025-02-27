def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[200]
    missing_sum = sum((n for n in range(a + 1, b) if n not in nums[61:201]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')