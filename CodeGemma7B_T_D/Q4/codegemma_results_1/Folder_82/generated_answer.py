def all_pos_ints_exclusive(nums):
    for i in range(20, 200):
        if i not in nums:
            nums.append(i)
    return nums