def all_pos_ints_exclusive(nums):
    rtn = []
    for num in nums[20:36]:
        if num > 0:
            rtn.append(num)
    return rtn or []