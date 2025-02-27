def all_pos_ints_exclusive(nums):
    pos_ints = []
    for num in nums[36:54]:
        if num > 0:
            pos_ints.append(num)
    return pos_ints if pos_ints else []