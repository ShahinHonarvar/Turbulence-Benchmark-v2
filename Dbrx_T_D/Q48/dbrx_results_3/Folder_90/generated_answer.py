def return_binary_or_hexa(nums):
    a, b = (nums[60], nums[90])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[60:91]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()