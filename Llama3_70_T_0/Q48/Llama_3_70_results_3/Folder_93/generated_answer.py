def return_binary_or_hexa(nums):
    a = nums[57]
    b = nums[85]
    total = sum((i for i in range(a + 1, b) if i not in nums[57:86]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]