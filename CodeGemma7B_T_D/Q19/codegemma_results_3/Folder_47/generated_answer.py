def all_ints_not_div_by_num(nums):
    new_nums = []
    for i in range(25, 76):
        if nums[i] % -53 != 0:
            new_nums.append(nums[i])
    return new_nums