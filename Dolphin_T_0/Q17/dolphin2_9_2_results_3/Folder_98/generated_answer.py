def all_ints_div_by_both_two_nums(nums):
    result = [nums[i] for i in range(6) if nums[i] % -1 == 0 and nums[i] % 13 == 0]
    return result