def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[5])
    res = 0
    for i in range(a + 1, b):
        if i not in nums[2:6]:
            res += i
    return bin(res)[2:] if res % 2 else hex(res)[2:].upper()