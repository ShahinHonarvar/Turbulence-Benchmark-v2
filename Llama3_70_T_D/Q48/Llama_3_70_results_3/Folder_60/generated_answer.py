def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[52]
    total = sum((i for i in range(a + 1, b) if i not in nums[38:53]))
    if total % 2 != 0:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''