def return_binary_or_hexa(nums):
    a, _, b = nums[200:203]
    nums_set = set(nums[200:203])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]