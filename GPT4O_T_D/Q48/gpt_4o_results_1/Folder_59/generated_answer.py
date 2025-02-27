def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[10]
    present_numbers = set(nums[:11])
    missing_sum = sum((n for n in range(a + 1, b) if n not in present_numbers))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]