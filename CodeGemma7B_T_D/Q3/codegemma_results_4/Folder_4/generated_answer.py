def all_pos_ints_inclusive(nums):
    pos_ints = [num for num in nums[12:93] if num > 0]
    return pos_ints if pos_ints else []