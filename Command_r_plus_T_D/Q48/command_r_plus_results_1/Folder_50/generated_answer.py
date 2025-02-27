def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[13], nums[76])
    sum_range = sum(range(a + 1, b))
    sum_nums = sum(set(range(a + 1, b)) - set(nums[13:76]))
    if sum_nums == sum_range:
        return ''
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()