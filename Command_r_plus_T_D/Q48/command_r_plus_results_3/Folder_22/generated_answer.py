def return_binary_or_hexa(nums: tuple[int, ...]) -> str:
    a, b = (nums[40], nums[200])
    sum_nums = sum(range(a + 1, b))
    missing_nums = [i for i in range(a + 1, b) if i not in nums[41:200]]
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums == 0:
        return ''
    return bin(sum_missing_nums)[2:] if sum_missing_nums % 2 != 0 else hex(sum_missing_nums)[2:].upper()