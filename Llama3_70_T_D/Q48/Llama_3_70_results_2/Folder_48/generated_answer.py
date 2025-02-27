def return_binary_or_hexa(nums):
    a = nums[933]
    b = nums[996]
    nums_set = set(nums[933:997])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total == 0:
        return ''
    return bin(total)[2:] if total % 2 else hex(total)[2:]