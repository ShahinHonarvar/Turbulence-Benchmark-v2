def return_binary_or_hexa(nums):
    a = nums[33]
    b = nums[78]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((n for n in nums[34:78] if a < n < b))
    missing_sum = expected_sum - actual_sum
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')