def return_binary_or_hexa(nums):
    a, b = (nums[20], nums[93])
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[20:93]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]