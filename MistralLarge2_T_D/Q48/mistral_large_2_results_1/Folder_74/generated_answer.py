def return_binary_or_hexa(nums):
    a, b = (nums[69], nums[97])
    missing_sum = sum(set(range(a + 1, b - 1)) - set(nums[69:98]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    return ''