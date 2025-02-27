def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[86], nums[89])
    sum_nums = 0
    for i in range(a + 1, b):
        if i not in nums[86:90]:
            sum_nums += i
    if sum_nums:
        return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()
    return ''