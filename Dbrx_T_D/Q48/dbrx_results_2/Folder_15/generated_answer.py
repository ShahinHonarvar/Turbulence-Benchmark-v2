def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[4])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[1:4]))
    if missing_sum % 2 == 1:
        return format(missing_sum, '08b')
    else:
        return format(missing_sum, 'x')