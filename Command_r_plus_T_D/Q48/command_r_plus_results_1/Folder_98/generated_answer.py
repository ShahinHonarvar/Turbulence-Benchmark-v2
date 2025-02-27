def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[6], nums[7])
    sum_nums = sum((i for i in range(a + 1, b) if i not in nums[6:8]))
    if sum_nums == 0:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 != 0 else hex(sum_nums)[2:].upper()