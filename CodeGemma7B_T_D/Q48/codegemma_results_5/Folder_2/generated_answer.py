def return_binary_or_hexa(nums):
    a, b = (nums[72], nums[93])
    res = 0
    for num in range(a + 1, b):
        if num not in nums[72:94]:
            res += num
    if res % 2 == 1:
        return bin(res)[2:]
    else:
        return hex(res)[2:].upper()