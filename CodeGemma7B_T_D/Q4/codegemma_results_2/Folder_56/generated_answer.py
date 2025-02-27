def all_pos_ints_exclusive(nums):
    ans = []
    for i in range(7, 9):
        if i >= 0 and i >= len(nums) or nums[i] < 0:
            continue
        ans.append(i)
    return ans