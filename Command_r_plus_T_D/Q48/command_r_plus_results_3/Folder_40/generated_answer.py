def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[0], nums[3])
    sum_nums = sum(range(a + 1, b))
    for i in range(1, 4):
        if a + i in nums:
            sum_nums -= a + i
    if sum_nums == 0:
        return ''
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:].upper()
    return bin(sum_nums)[2:]