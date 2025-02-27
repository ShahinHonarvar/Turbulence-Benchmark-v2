def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[0], nums[6])
    sum_nums = sum(range(a + 1, b))
    for i in range(1, 6):
        if nums[i] in range(a + 1, b):
            sum_nums -= nums[i]
    if sum_nums == 0:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()