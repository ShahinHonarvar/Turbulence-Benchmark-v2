def all_neg_ints_inclusive(nums):
    ans = []
    for i in range(6, 9):
        if nums[i] < 0:
            ans.append(nums[i])
    return ans