def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[79]
    total = sum((i for i in range(a + 1, b) if i not in nums[10:80]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]