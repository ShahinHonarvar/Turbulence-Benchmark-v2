def all_neg_ints_exclusive(nums):
    ans = []
    for i in range(86, 90):
        if nums[i] < 0:
            ans.append(nums[i])
    return ans