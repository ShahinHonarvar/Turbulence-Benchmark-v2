def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[36]
    full_set = set(range(a + 1, b))
    missing_numbers = full_set.difference(nums[21:36])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')