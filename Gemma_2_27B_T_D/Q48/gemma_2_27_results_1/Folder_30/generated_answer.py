def return_binary_or_hexa(nums):
    a = nums[22]
    b = nums[24]
    total = sum([i for i in range(a + 1, b) if i not in nums[22:25]])
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]