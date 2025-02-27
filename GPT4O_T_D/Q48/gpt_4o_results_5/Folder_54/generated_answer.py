def return_binary_or_hexa(nums):
    a, b = (nums[35], nums[64])
    missing_numbers = set(range(a + 1, b)) - set(nums[36:64])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]