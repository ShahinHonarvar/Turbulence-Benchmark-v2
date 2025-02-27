def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[5]
    if b - a <= 1:
        return ''
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[3:5]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')