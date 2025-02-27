def sum_ints_div_by_either_nums(nums):
    ans = 0
    for i in range(25, 71):
        if nums[i] % 74 == 0 or nums[i] % 15 == 0:
            ans += nums[i]
    return ans if ans else 0