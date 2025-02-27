def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[52]
    total = sum((i for i in range(a + 1, b) if i not in nums[38:53]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]