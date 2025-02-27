def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[4]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum += i
    if sum == 0:
        return ''
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]