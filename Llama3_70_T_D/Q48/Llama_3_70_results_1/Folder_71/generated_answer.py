def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[35]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[21:36]))
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]