def return_binary_or_hexa(nums):
    a, b = (nums[7], nums[9])
    total = sum((i for i in range(a + 1, b) if i not in nums[7:10]))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]