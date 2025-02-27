def return_binary_or_hexa(nums):
    a = nums[51]
    b = nums[76]
    total = sum((i for i in range(a + 1, b) if i not in nums[51:77]))
    if total % 2 == 1:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]