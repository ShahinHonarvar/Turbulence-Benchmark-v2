def all_ints_div_by_both_two_nums(nums):
    ans = []
    for i in range(828, 933):
        if nums[i] % -649 == 0 and nums[i] % -461 == 0:
            ans.append(nums[i])
    return ans