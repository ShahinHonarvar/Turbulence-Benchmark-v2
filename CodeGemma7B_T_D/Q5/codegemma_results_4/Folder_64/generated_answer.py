def all_neg_ints_inclusive(nums):
    ans = []
    for num in nums:
        if -4 <= num <= 4:
            ans.append(num)
    return ans