def return_binary_or_hexa(nums):
    a, b = (nums[36], nums[52])
    missing_numbers = set(range(a + 1, b)) - set(nums[37:52])
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]