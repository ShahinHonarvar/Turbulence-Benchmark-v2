def sum_ints_div_by_either_nums(nums):
    ans = 0
    for i in range(69, 100):
        if i % -37 == 0 or i % -26 == 0:
            ans += nums[i]
    return ans