def sum_ints_div_by_either_nums(nums):
    ans = 0
    for i in range(50, 201):
        if nums[i] % 64 == 0 or nums[i] % 34 == 0:
            ans += nums[i]
    return ans or 0