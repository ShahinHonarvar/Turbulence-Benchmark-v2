def return_binary_or_hexa(nums):
    a = nums[77]
    b = nums[84]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[78:84]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')