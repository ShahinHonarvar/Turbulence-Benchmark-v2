def return_binary_or_hexa(nums):
    a = nums[86]
    b = nums[99]
    missing = set(range(a + 1, b)) - set(nums[86 + 1:99])
    missing_sum = sum(missing)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    else:
        return ''