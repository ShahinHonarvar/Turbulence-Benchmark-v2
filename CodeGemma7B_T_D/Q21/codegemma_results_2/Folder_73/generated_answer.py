def all_ints_div_by_num(nums):
    ans = []
    for i in range(18, 39):
        if nums[i] % -97 == 0:
            ans.append(nums[i])
    return ans or []