def all_ints_div_by_both_two_nums(nums):
    ans = []
    for i in nums[36:86]:
        if i % -27 == 0 and i % -96 == 0:
            ans.append(i)
    return ans