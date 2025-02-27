def return_binary_or_hexa(nums):
    a = nums[25]
    b = nums[80]
    missing_numbers = [num for num in range(a + 1, b) if num not in nums[25:81]]
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2:
        return format(sum_missing, '08b')
    return format(sum_missing, 'x')