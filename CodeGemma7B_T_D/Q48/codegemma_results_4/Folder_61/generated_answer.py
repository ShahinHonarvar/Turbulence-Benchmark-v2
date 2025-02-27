def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[8])
    total = sum(range(a + 1, b))
    res = ''
    for x in range(a + 1, b):
        if x not in nums:
            res += str(x)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].lower() if total < 16 else hex(total)[2:]