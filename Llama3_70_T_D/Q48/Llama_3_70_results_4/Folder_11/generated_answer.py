def return_binary_or_hexa(nums):
    a = nums[48]
    b = nums[76]
    nums_set = set(nums[48:77])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]