def return_binary_or_hexa(nums):
    a = nums[15]
    b = nums[57]
    total = sum((i for i in range(a + 1, b) if i not in nums[15:58]))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]