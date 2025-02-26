def all_pos_ints_inclusive(nums):
    if len(nums) <= 95:
        return []
    slice_list = nums[74:96]
    positive_ints = [num for num in slice_list if num > 0]
    return positive_ints