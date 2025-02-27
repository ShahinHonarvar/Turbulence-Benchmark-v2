def return_binary_or_hexa(nums):
    a, b = (nums[34], nums[69])
    subset = set(nums[34:70])
    missing_sum = sum((x for x in range(a + 1, b) if x not in subset))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]