def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[79]
    s = sum(range(a + 1, b)) - sum(nums[10:80])
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]