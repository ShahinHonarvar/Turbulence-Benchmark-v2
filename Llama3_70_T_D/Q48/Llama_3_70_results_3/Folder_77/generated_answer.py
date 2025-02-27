def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[52]
    nums_set = set(nums[18:53])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum != 0:
        return hex(total_sum)[2:]
    else:
        return ''