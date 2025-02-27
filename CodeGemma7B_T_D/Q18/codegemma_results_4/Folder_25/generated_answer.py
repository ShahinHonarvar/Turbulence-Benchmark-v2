def sum_ints_div_by_either_nums(nums):
    ans = 0
    for i in range(25, 81):
        if nums[i] % 20 == 0 or nums[i] % 26 == 0:
            ans += nums[i]
    if ans == 0:
        return 0
    else:
        return ans