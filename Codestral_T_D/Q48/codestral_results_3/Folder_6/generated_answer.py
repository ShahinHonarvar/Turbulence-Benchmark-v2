def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[93]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[20:94]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]