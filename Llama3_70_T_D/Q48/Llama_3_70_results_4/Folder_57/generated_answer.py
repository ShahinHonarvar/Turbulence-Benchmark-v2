def return_binary_or_hexa(nums):
    a = nums[25]
    b = nums[80]
    total = sum((i for i in range(a + 1, b) if i not in nums[26:81]))
    return bin(total)[2:] if total % 2 else hex(total)[2:]