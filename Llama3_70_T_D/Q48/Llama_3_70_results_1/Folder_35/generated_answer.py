def return_binary_or_hexa(nums):
    a = nums[77]
    b = nums[84]
    nums_set = set(nums[77:85])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]