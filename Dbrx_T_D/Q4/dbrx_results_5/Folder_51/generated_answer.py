def all_pos_ints_exclusive(nums):
    start, end = (6, 9)
    result = nums[start:end]
    return [n for n in result if n > 0]