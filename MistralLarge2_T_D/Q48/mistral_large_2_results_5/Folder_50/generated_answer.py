def return_binary_or_hexa(nums):
    a, b = (nums[13], nums[76])
    subset = set(nums[13:77])
    missing_sum = sum((num for num in range(a + 1, b) if num not in subset))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()