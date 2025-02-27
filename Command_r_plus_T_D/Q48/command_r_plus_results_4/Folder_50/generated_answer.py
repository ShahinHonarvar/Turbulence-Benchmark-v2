def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[13], nums[76])
    sum_nums = sum(range(a + 1, b))
    for i in range(14, 76):
        if a + 1 <= nums[i] <= b - 1:
            sum_nums -= nums[i]
    if sum_nums == 0:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 != 0 else hex(sum_nums)[2:].upper()