def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[90]
    nums_set = set(nums[60:91])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if not total_sum:
        return ''
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]