def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for i in range(73, 87):
        if nums[i] % 54 == 0 and nums[i] % 82 == 0:
            divisible_nums.append(nums[i])
    return divisible_nums