def return_binary_or_hexa(nums):
    a = nums[17]
    b = nums[88]
    total = sum((i for i in range(a + 1, b) if i not in nums[17:89]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]