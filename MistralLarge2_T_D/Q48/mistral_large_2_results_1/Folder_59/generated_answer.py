def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[10])
    existing_numbers = set(nums[:11])
    missing_sum = sum((x for x in range(a + 1, b) if x not in existing_numbers))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()