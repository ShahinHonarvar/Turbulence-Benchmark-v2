def return_binary_or_hexa(nums):
    a, b = (nums[10], nums[76])
    missing_nums = set(range(a + 1, b)) - set(nums[10:77])
    total_sum = sum(missing_nums)
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]