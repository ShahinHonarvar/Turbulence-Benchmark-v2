def all_pos_ints_inclusive(nums):
    i = 62
    ans = []
    while i <= 92:
        if i in range(63, 93):
            ans.append(nums[i])
        i += 1
    return ans