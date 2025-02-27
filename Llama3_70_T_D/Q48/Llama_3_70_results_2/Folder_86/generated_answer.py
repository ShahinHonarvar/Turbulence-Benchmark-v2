def return_binary_or_hexa(nums):
    a = nums[19]
    b = nums[32]
    total = sum((i for i in range(a + 1, b) if i not in nums[19:33]))
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:]