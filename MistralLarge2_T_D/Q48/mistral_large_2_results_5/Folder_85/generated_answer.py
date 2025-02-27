def return_binary_or_hexa(nums):
    a, b = (nums[1], nums[8])
    existing = set(nums[1:9])
    missing_sum = sum((x for x in range(a + 1, b) if x not in existing))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()