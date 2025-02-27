def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[3])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[:4]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]