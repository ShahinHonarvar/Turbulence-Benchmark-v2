def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[76]
    s = sum((i for i in range(a + 1, b) if i not in nums[10:77]))
    if s == 0:
        return ''
    return bin(s)[2:] if s % 2 else hex(s)[2:]