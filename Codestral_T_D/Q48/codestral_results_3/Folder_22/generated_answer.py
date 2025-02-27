def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200]
    missing = set(range(a + 1, b)) - set(nums[40:201])
    s = sum(missing)
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]