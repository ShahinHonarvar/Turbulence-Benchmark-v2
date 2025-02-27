def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[100])
    non_present = set(range(a + 1, b)) - set(nums[10:100])
    if not non_present:
        return ''
    total_sum = sum(non_present)
    if total_sum % 2:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')