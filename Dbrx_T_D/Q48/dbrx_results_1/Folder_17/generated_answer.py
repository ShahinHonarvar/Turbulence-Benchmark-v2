def return_binary_or_hexa(nums):
    a = nums[73]
    b = nums[84]
    missing_sum = sum((i for i in range(a + 1, b) if nums[73:85] != list(range(nums[73], nums[84] + 1))))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()