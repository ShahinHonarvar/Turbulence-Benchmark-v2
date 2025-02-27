def return_binary_or_hexa(nums):
    a = nums[37]
    b = nums[43]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[37:44]))
    return bin(total_sum)[2:] if total_sum & 1 else hex(total_sum)[2:]