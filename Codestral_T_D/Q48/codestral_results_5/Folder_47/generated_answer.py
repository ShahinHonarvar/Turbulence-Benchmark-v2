def return_binary_or_hexa(nums):
    a, b = (nums[29], nums[53])
    missing_nums = set(range(a + 1, b)) - set(nums[29 + 1:53])
    total_sum = sum(missing_nums)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]