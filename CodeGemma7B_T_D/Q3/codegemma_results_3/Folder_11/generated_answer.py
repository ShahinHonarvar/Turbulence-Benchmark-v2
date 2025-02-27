def all_pos_ints_inclusive(nums):
    pos_ints = []
    for num in nums[37:52]:
        if num > 0:
            pos_ints.append(num)
    return pos_ints or []