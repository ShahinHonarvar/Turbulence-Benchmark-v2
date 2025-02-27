def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[9])
    full_set = set(range(a + 1, b))
    present_set = set(nums[1:9])
    missing_nums = sorted(list(full_set - present_set))
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]