def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[60]
    total = 0
    for i in range(a + 1, b):
        if i not in nums[18:60]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()