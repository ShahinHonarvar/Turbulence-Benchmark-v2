def return_binary_or_hexa(nums):
    a = nums[2]
    b = nums[8]
    nums_set = set(nums[2:9])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    if not total:
        return ''
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:]