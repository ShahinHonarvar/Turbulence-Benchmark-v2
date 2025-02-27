def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[110], nums[348])
    sum_nums = 0
    for i in range(a + 1, b):
        if i not in nums[110:348]:
            sum_nums += i
    if sum_nums == 0:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 != 0 else hex(sum_nums)[2:].upper()