def all_neg_ints_inclusive(nums):
    ans = []
    for n in nums[4:5]:
        if n <= 0:
            ans.append(n)
    return ans