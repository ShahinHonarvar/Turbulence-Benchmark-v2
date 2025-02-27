def all_ints_not_div_by_num(nums):
    not_divisible = []
    for i in range(4, 5):
        if nums[i] % -7 != 0:
            not_divisible.append(nums[i])
    return not_divisible