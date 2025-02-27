def return_binary_or_hexa(nums):
    a = nums[34]
    b = nums[69]
    total = sum((i for i in range(a + 1, b) if i not in nums[35:70]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]