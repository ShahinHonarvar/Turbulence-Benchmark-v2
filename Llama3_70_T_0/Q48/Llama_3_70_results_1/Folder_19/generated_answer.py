def return_binary_or_hexa(nums):
    a = nums[1]
    b = nums[4]
    total = sum((i for i in range(a + 1, b) if i not in nums[1:5]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]