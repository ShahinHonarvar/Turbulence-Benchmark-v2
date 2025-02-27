def return_binary_or_hexa(nums):
    a, b = (nums[1], nums[4])
    sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum += i
    if sum % 2 == 1:
        return f'{sum:b}'
    else:
        return f'{sum:x}'