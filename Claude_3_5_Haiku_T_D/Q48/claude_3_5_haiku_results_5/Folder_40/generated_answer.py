def return_binary_or_hexa(nums):
    a, b = (nums[0], nums[3])
    excluded_nums = set(nums[0:4])
    sum_excluded = sum((num for num in range(a + 1, b) if num not in excluded_nums))
    if sum_excluded == 0:
        return ''
    if sum_excluded % 2 == 1:
        return bin(sum_excluded)[2:]
    else:
        return hex(sum_excluded)[2:]