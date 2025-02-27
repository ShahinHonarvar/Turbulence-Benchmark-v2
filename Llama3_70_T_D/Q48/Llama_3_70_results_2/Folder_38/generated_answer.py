def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[85]
    nums_set = set(nums[36:86])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]