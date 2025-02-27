def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[76]
    s = sum((i for i in range(a + 1, b) if i not in nums[10:77]))
    if s % 2 == 1:
        return bin(s)[2:]
    elif s != 0:
        return hex(s)[2:]
    else:
        return ''