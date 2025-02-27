def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[84]
    total = sum((i for i in range(a + 1, b) if i not in nums[57:85]))
    if total % 2 == 1:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''