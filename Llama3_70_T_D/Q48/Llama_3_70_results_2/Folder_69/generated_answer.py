def return_binary_or_hexa(nums):
    a = nums[39]
    b = nums[43]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[39:44]))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]