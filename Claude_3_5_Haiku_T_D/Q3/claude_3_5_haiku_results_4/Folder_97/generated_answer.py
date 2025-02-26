def all_pos_ints_inclusive(nums):
    if len(nums) <= 80:
        return []
    return [x for x in nums[40:81] if x > 0]