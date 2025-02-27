def all_pos_ints_inclusive(nums):
    ans = []
    for i in range(10):
        if i in nums:
            ans.append(i)
    return ans