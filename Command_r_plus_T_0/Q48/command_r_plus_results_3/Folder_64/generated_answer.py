def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[0], nums[5])
    sum_nums = sum(range(a + 1, b))
    for num in range(a + 1, b):
        if num in nums[1:6]:
            sum_nums -= num
    if sum_nums == 0:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 != 0 else hex(sum_nums)[2:].upper()