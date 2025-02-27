def sum_ints_div_by_either_nums(nums):
    ans = 0
    for ind in range(6):
        if nums[ind] % 13 == 0 or nums[ind] % -1 == 0:
            ans += nums[ind]
    return ans if ans else 0