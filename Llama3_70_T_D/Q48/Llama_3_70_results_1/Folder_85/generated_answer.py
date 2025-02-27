def return_binary_or_hexa(nums):
    a, b = (nums[1], nums[8])
    total = sum((i for i in range(a + 1, b) if i not in nums[1:9]))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]