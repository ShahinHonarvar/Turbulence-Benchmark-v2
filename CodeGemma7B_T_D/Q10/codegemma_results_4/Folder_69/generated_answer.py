def all_odd_ints_exclusive(nums):
    if not nums or (68 > max(nums) or 0 > min(nums)):
        return []
    return [x for x in nums[68:99] if x % 2]