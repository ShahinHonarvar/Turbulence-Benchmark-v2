def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[90]
    total = 0
    for i in range(a + 1, b):
        if i not in nums[60:91]:
            total += i
    if total % 2 != 0:
        return bin(total)[2:]
    elif total == 0:
        return ''
    else:
        return hex(total)[2:]