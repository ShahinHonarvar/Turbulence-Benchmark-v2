def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[10], nums[28])
    range_nums = set(nums[10:29])
    sum_nums = 0
    for num in range(a + 1, b):
        if num not in range_nums:
            sum_nums += num
    if sum_nums:
        return bin(sum_nums)[2:] if sum_nums % 2 else hex(sum_nums)[2:].upper()
    else:
        return ''