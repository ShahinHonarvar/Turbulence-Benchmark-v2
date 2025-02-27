def return_binary_or_hexa(nums):
    a, b = (nums[57], nums[84])
    total = sum((i for i in range(a + 1, b) if i not in nums[57:85]))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]