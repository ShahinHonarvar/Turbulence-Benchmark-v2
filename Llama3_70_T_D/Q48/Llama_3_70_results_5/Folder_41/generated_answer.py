def return_binary_or_hexa(nums):
    a = nums[3]
    b = nums[8]
    nums_set = set(nums[3:9])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total == 0:
        return ''
    if total % 2 != 0:
        return bin(total)[2:]
    return hex(total)[2:]