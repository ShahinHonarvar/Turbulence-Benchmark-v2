def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[35]
    total = sum((i for i in range(a + 1, b) if i not in nums[20:36]))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]