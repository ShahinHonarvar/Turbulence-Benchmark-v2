def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    nums_set = set(nums[86:100])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]