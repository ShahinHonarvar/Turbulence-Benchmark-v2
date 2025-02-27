def all_ints_div_by_both_two_nums(nums):
    divisible_ints = []
    for i in range(38, 82):
        if nums[i] % -61 == 0 and nums[i] % -71 == 0:
            divisible_ints.append(nums[i])
    return divisible_ints