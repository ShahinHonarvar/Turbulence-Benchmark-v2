def return_binary_or_hexa(nums):
    a = nums[46]
    b = nums[91]
    nums_set = set(nums[46:92])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]