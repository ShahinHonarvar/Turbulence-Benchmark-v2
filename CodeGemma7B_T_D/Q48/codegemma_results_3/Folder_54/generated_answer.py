def return_binary_or_hexa(nums):
    a, b = (nums[35], nums[64])
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[35:65]:
            sum += i
    if sum % 2 == 0:
        return f'{sum:x}'
    else:
        return f'{sum:b}'