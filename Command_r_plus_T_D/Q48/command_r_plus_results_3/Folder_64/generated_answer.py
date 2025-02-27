def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[0], nums[5])
    sum_nums = sum(range(a + 1, b))
    for i in range(1, 5):
        if a + i in nums:
            sum_nums -= a + i
    if sum_nums in nums:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 != 0 else hex(sum_nums)[2:].upper()