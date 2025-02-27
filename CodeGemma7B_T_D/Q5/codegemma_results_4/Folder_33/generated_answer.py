def all_neg_ints_inclusive(nums):
    ans = []
    for num in nums[667:775]:
        if num < 0:
            ans.append(num)
    return ans