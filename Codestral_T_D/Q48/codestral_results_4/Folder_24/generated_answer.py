def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[91]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[13:92]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]