def return_binary_or_hexa(nums):
    a = nums[48]
    b = nums[76]
    nums_set = set(nums[48:77])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if not total_sum:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]