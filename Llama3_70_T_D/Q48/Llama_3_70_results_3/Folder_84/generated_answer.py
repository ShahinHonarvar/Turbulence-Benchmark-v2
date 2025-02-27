def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[44]
    total = sum((i for i in range(a + 1, b) if i not in nums[32:45]))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]