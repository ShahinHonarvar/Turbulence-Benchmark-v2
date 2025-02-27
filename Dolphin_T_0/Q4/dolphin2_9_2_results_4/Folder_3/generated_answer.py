def all_pos_ints_exclusive(nums):
    return [num for i, num in enumerate(nums[78:94]) if i > 0 and i < len(nums[78:94]) - 2 and (num > 0)]