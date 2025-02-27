def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[52]
    nums_set = set(nums[36:53])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]