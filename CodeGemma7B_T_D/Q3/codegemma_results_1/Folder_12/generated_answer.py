def all_pos_ints_inclusive(nums):
    new_list = []
    for i in range(14, 65):
        if nums[i] > 0:
            new_list.append(nums[i])
    return new_list or []