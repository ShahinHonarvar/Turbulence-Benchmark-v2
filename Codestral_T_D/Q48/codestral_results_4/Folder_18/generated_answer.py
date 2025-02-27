def return_binary_or_hexa(nums):
    a, b = (nums[56], nums[90])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[56:90]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]