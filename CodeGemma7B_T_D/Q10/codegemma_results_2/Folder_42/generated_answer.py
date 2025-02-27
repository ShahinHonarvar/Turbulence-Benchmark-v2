def all_odd_ints_exclusive(nums):
    if not nums or len(nums) < 68:
        return []
    return [num for num in nums[44:67] if num % 2 != 0]