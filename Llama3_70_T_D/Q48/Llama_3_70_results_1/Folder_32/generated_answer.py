def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[90]
    total_sum = sum((i for i in range(a + 1, b) if i not in nums[86:91]))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]