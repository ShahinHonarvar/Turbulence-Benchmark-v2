def all_odd_ints_inclusive(nums):
    if not nums or len(nums) < 6:
        return []
    return nums[0:7:2]