def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    range_nums = set(nums[30:201])
    if all((x in range_nums for x in range(a + 1, b))):
        return ''
    missing_nums_sum = sum((x for x in range(a + 1, b) if x not in nums[30:201]))
    if missing_nums_sum % 2 == 1:
        return bin(missing_nums_sum)[2:]
    else:
        return hex(missing_nums_sum)[2:].upper()