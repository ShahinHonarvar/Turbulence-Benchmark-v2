def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    total = sum((i for i in range(a + 1, b) if i not in nums[57:90]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]