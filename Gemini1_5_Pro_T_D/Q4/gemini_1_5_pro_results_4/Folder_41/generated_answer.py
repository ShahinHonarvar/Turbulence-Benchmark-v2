def all_pos_ints_exclusive(nums):
    pos_ints = []
    for i in range(max(8, 0), min(9, len(nums))):
        if nums[i] > 0:
            pos_ints.append(nums[i])
    return pos_ints