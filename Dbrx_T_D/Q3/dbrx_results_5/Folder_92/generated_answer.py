def all_pos_ints_inclusive(nums):
    if not nums or len(nums) < 2 or nums[0] <= 0:
        return []
    return [num for num in nums if 0 < num <= nums[1]]