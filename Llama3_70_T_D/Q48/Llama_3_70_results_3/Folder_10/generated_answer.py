def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[54]
    nums_set = set(nums[36:55])
    total = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total == 0:
        return ''
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]