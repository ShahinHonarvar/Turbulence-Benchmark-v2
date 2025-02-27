def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[0], nums[2])
    sum_nums = sum(range(a + 1, b))
    missing_nums = set(range(a + 1, b)).difference(nums[1:3])
    if missing_nums:
        sum_missing_nums = sum(missing_nums)
        if sum_missing_nums % 2 == 1:
            return bin(sum_missing_nums)[2:]
        else:
            return hex(sum_missing_nums)[2:].upper()
    else:
        return ''