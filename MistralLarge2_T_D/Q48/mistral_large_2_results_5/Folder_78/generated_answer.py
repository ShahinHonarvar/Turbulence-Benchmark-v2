def return_binary_or_hexa(nums):
    a = nums[62]
    b = nums[96]
    missing_sum = sum((x for x in range(a + 1, b) if x not in set(nums[62:97])))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]