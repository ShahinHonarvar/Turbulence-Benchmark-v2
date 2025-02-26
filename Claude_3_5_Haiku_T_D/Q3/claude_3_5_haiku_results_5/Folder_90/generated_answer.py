def all_pos_ints_inclusive(nums):
    if len(nums) <= 746:
        return []
    subset = nums[262:747]
    return [x for x in subset if x > 0]