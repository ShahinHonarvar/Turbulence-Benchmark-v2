def return_binary_or_hexa(nums):
    a = nums[45]
    b = nums[48]
    nums_set = set(nums[45:49])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if all((i in nums_set for i in range(a + 1, b))):
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]