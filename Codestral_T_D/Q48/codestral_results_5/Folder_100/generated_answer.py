def return_binary_or_hexa(nums):
    a, b = (nums[44], nums[78])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[44 + 1:78]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]