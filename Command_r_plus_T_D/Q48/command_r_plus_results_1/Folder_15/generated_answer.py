def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[0], nums[4])
    sum_nums = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)).difference(set(nums[:5]))
    if not missing_nums:
        return ''
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()