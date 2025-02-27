def all_pos_ints_exclusive(nums):
    pos_ints = []
    if len(nums) > 201:
        for i in range(21, 200):
            if nums[i] > 0:
                pos_ints.append(nums[i])
    return pos_ints