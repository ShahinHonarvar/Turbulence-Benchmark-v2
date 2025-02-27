def return_binary_or_hexa(nums):
    a = nums[37]
    b = nums[43]
    sum = 0
    for i in range(a + 1, b):
        if i not in nums[37:44]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()