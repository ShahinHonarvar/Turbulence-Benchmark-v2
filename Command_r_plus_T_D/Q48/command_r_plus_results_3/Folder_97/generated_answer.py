def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[34], nums[69])
    sum_range = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)) - set(nums[35:69])
    sum_missing = sum(missing_nums)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()