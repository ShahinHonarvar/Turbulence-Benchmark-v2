def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[52]
    missing_sum = sum(set(range(a + 1, b)).difference(nums[38:53]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    return ''