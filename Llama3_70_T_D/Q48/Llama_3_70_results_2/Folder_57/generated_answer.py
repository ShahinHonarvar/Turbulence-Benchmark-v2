def return_binary_or_hexa(nums):
    a = nums[25]
    b = nums[80]
    s = sum((i for i in range(a + 1, b) if i not in nums[25:81]))
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]