def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[70]
    all_numbers = set(range(a + 1, b))
    existing_numbers = set(nums[14:70])
    missing_numbers = all_numbers - existing_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return format(total_sum, 'X')
    else:
        return format(total_sum, 'b')