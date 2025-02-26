def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for i in range(154, 799):
        if i < len(nums) and nums[i] % 275 == 0 and (nums[i] % 580 == 0):
            divisible_nums.append(nums[i])
    return divisible_nums