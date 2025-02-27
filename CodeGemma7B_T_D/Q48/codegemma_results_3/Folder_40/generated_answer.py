def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[3])
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[0:4]:
            sum += i
    if sum % 2:
        return format(sum, 'b')
    else:
        return format(sum, 'x')