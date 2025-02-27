def return_binary_or_hexa(nums):
    a = nums[110]
    b = nums[348]
    total = sum((i for i in range(a + 1, b) if i not in nums[111:348]))
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]