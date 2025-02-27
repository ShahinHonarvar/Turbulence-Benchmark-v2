def return_binary_or_hexa(nums):
    a, b = (nums[60], nums[200])
    range_nums = set(nums[60:201])
    missing_sum = sum((i for i in range(a + 1, b) if i not in range_nums))
    if not missing_sum:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]