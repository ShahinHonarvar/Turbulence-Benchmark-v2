def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[10], nums[100])
    sum_nums = sum((i for i in range(a + 1, b) if i not in nums[10:100]))
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]