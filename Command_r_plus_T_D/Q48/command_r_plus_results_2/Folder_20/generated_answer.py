def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[27], nums[96])
    sum_nums = sum((i for i in range(a + 1, b) if i not in nums[28:96]))
    if sum_nums in nums[28:96]:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 != 0 else hex(sum_nums)[2:].upper()