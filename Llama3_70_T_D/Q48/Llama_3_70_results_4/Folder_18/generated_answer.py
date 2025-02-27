def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[90]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[56:91]))
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]