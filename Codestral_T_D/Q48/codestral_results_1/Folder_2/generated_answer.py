def return_binary_or_hexa(nums):
    a = nums[72]
    b = nums[93]
    subset = set(nums[72 + 1:93])
    missing_nums = set(range(a + 1, b)) - subset
    total_sum = sum(missing_nums)
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]