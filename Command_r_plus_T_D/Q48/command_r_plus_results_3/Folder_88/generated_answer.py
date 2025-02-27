def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[3], nums[9])
    sum_nums = sum(range(a + 1, b))
    if sum_nums in nums[3:10]:
        return ''
    elif sum_nums % 2 == 0:
        return hex(sum_nums)[2:].upper()
    else:
        return bin(sum_nums)[2:]