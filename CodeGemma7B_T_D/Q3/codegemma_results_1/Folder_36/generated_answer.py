def all_pos_ints_inclusive(nums):
    if not nums or max(nums) <= 0:
        return []
    return [i for i in range(246, 751) if i in nums]