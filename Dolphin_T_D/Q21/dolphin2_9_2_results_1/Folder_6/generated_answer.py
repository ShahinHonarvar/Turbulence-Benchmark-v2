def all_ints_div_by_num(nums):
    divisible_nums = []
    for i in range(13, 64):
        if nums[i] % 46 == 0:
            divisible_nums.append(nums[i])
    return divisible_nums