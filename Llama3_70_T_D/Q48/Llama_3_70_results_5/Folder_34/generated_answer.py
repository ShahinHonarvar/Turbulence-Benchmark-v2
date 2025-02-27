def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[200]
    s = sum((i for i in range(a + 1, b) if i not in nums[61:200]))
    if s % 2 == 1:
        return bin(s)[2:]
    elif s:
        return hex(s)[2:]
    else:
        return ''