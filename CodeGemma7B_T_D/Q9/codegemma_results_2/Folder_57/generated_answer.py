def all_odd_ints_inclusive(nums):
    if not nums or nums[27] % 2 == 0 or nums[55] % 2 == 0:
        return []
    return nums[27:56:2]