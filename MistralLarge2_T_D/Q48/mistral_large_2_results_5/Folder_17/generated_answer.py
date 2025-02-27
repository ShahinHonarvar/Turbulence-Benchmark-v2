def return_binary_or_hexa(nums):
    a = nums[73]
    b = nums[84]
    subset = set(nums[73:85])
    missing_sum = sum((x for x in range(a + 1, b) if x not in subset))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()