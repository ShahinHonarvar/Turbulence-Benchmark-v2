def all_pos_ints_exclusive(nums):
    temp = []
    for num in nums:
        if num > 0 and nums.index(num) >= 743 and (nums.index(num) < 867):
            temp.append(num)
    return temp or []