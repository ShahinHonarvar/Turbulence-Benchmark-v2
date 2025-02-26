def all_pos_ints_inclusive(nums):
    if len(nums) <= 94:
        return []
    return [x for x in nums[75:95] if x > 0]