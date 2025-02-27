def return_binary_or_hexa(nums):
    a = nums[90]
    b = nums[97]
    total = sum((i for i in range(a + 1, b) if i not in nums[91:97]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]