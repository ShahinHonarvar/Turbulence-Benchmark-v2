def return_binary_or_hexa(nums):
    a = nums[72]
    b = nums[93]
    total = sum(range(a + 1, b))
    actual = sum((x for x in nums[73:93] if a < x < b))
    diff = total - actual
    if diff == 0:
        return ''
    elif diff % 2 == 1:
        return bin(diff)[2:]
    else:
        return hex(diff)[2:]