def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[52]
    set_nums = set(nums[38:53])
    total = sum((i for i in range(a + 1, b) if i not in set_nums))
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]