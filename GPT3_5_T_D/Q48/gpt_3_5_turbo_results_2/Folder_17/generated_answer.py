def return_binary_or_hexa(nums):
    a = nums[73]
    b = nums[84]
    if all((i in nums[73:85] for i in range(a + 1, b))):
        return ''
    total = sum((i for i in range(a + 1, b) if i not in nums[73:85]))
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]