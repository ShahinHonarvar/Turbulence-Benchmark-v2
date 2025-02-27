def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[28])
    nums_set = set(nums[10:29])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_set))
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]