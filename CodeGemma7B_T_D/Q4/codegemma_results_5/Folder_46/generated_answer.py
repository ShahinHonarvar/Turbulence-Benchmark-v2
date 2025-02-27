def all_pos_ints_exclusive(nums):
    pos_int_list = []
    for num in nums[20:44]:
        if num > 0:
            pos_int_list.append(num)
    return pos_int_list or []