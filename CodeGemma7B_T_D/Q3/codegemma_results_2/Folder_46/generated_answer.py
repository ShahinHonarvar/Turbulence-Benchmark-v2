def all_pos_ints_inclusive(nums):
    pos_ints = []
    for i in range(30, 88):
        if i in nums:
            pos_ints.append(i)
    return pos_ints