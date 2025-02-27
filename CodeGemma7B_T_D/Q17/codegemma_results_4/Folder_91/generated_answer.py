def all_ints_div_by_both_two_nums(nums):
    ans = []
    for i in range(5):
        if nums[i] % 8 == 0 and nums[i] % -3 == 0:
            ans.append(nums[i])
    return ans