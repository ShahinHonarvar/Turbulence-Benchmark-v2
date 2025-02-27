def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[7])
    missing_nums = set(range(a + 1, b)) - set(nums[2:7])
    s = sum(missing_nums)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''