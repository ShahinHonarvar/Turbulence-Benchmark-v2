def return_binary_or_hexa(nums):
    a, b = (nums[3], nums[9])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[3:9]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]