def return_binary_or_hexa(nums):
    a = nums[42]
    b = nums[87]
    s = sum([i for i in range(a + 1, b) if i not in nums[42:87]])
    if s % 2 != 0:
        return bin(s)[2:]
    else:
        return hex(s)[2:]