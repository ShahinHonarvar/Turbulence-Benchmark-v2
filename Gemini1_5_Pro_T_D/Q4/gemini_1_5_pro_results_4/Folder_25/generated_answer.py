def all_pos_ints_exclusive(nums):
    pos_nums = []
    for i in range(41, 69):
        if i >= len(nums):
            break
        if nums[i] > 0:
            pos_nums.append(nums[i])
    return pos_nums