def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[70]
    num_set = set(nums[14:70])
    missing_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')