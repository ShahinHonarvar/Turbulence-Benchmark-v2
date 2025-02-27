def return_binary_or_hexa(nums):
    a, b = (nums[48], nums[76])
    subset = set(nums[48:77])
    missing_sum = sum((x for x in range(a + 1, b) if x not in subset))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()