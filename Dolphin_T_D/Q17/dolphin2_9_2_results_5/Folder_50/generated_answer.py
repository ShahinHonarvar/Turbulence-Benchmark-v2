def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for i in range(46, 92):
        if nums[i] % 67 == 0 and nums[i] % 15 == 0:
            divisible_nums.append(nums[i])
    return divisible_nums