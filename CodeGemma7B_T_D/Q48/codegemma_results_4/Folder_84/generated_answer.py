def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[44]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[32:44]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]