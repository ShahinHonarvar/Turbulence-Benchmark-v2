def all_neg_ints_inclusive(nums):
    ans = []
    for i in range(3, 6):
        if nums[i] < 0:
            ans.append(nums[i])
    return ans