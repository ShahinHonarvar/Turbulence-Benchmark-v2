def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[0], nums[3])
    sum_nums = sum(range(a + 1, b))
    for i in range(1, 4):
        if nums[i] in range(a + 1, b):
            sum_nums -= nums[i]
    if sum_nums == 0:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 != 0 else hex(sum_nums)[2:].upper()