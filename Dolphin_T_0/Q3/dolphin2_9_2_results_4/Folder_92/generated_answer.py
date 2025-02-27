def all_pos_ints_inclusive(nums):
    pos_nums = []
    for num in nums[0:2]:
        if num > 0:
            pos_nums.append(num)
    return pos_nums