def return_binary_or_hexa(nums):
    a, b = (nums[7], nums[9])
    missing = set(range(a + 1, b)) - set(nums[7:10])
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    elif s > 0:
        return hex(s)[2:]
    else:
        return ''