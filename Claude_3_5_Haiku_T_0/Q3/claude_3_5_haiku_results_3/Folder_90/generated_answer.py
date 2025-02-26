def all_pos_ints_inclusive(nums):
    if len(nums) <= 746:
        return []
    result = [num for num in nums[262:747] if num > 0]
    return result