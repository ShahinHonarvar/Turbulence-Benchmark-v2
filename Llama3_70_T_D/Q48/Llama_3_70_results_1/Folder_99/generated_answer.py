def return_binary_or_hexa(nums):
    a = nums[427]
    b = nums[669]
    nums_set = set(nums[427:670])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]