def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[93]
    missing_sum = 0
    for number in range(a + 1, b):
        if number not in nums[21:94]:
            missing_sum += number
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return format(missing_sum, 'x')
    else:
        return format(missing_sum, 'b')