def all_ints_div_by_num(nums):
    ans = []
    for i in range(816, 884):
        if nums[i] % 586 == 0:
            ans.append(nums[i])
    return ans