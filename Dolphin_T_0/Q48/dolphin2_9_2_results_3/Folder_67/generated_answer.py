def return_binary_or_hexa(nums):
    a, b = (nums[44], nums[67])
    missing_sum = sum((x for x in range(a + 1, b) if x not in nums[44:68]))
    result = ''
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 0:
        result = hex(missing_sum)[2:]
    else:
        result = bin(missing_sum)[2:]
    return result