def all_pos_ints_inclusive(nums):
    if len(nums) <= 975:
        return []
    result = [num for num in nums[639:976] if num > 0]
    return result