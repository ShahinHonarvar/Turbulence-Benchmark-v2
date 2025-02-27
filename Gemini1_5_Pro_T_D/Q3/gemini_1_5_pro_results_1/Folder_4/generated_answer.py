def all_pos_ints_inclusive(nums):
    pos_ints = []
    if len(nums) >= 93:
        for i in range(12, 93):
            if nums[i] > 0:
                pos_ints.append(nums[i])
    return pos_ints