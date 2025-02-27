def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[5]
    total = sum((i for i in range(a + 1, b) if i not in nums))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]