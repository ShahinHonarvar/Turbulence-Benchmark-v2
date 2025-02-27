def return_binary_or_hexa(nums):
    a, b = (nums[29], nums[53])
    s = sum((i for i in range(a + 1, b) if i not in nums))
    if s % 2:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()