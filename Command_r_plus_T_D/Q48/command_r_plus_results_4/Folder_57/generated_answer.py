def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[25], nums[80])
    range_nums = set(nums[26:81])
    sum_nums = sum((i for i in range(a + 1, b) if i not in range_nums))
    if sum_nums in range_nums:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()