def all_ints_div_by_num(nums):
    ans = []
    for i in range(319, 613):
        if nums[i] % 215 == 0:
            ans.append(nums[i])
    return ans