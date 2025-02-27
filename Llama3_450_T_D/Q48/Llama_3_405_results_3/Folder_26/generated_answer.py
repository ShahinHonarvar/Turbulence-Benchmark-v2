def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    s = set(range(a + 1, b))
    t = set(nums[69:99])
    total = sum(s - t)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]