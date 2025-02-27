def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[52]
    total = sum((i for i in range(a + 1, b) if i not in nums[36:53]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]