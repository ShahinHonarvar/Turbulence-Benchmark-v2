def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[10], nums[28])
    sum_nums = sum((i for i in range(a + 1, b) if i not in nums[10:28]))
    if sum_nums in nums[10:28]:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()