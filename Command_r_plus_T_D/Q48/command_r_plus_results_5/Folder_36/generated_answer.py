def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[110], nums[348])
    sum_nums = sum(range(a + 1, b))
    if sum_nums in nums[110:349]:
        return ''
    return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()