def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    s = sum((i for i in range(a + 1, b) if i not in nums[86:100]))
    if s == 0:
        return ''
    if s % 2 == 1:
        return bin(s)[2:]
    return hex(s)[2:]