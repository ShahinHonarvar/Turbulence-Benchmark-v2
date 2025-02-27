def return_binary_or_hexa(nums):
    a, b = (nums[3], nums[8])
    nums_range = set(nums[3:9])
    total_sum = sum((i for i in range(a + 1, b) if i not in nums_range))
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]