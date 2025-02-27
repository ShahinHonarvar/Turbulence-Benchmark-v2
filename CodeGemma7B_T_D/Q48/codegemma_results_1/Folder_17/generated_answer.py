def return_binary_or_hexa(nums):
    a, b = (nums[73], nums[84])
    res = sum((i for i in range(a + 1, b - 1 + 1) if i not in nums[73:85]))
    return bin(res)[2:] if res % 2 else hex(res)[2:].upper()