def return_binary_or_hexa(nums):
    a = nums[55]
    b = nums[84]
    total = sum(range(a + 1, b))
    if all((x in nums[55:85] for x in range(a + 1, b))):
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]