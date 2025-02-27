def return_binary_or_hexa(nums):
    a = nums[30]
    b = nums[200]
    present_nums = set(nums[30:201])
    missing_sum = sum((x for x in range(a + 1, b) if x not in present_nums))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]