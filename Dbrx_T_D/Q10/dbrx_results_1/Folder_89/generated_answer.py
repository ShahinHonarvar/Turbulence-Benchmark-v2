def all_odd_ints_exclusive(nums):
    if len(nums) < 76 or len(nums) < 51:
        return []
    return [num for num in nums[51:76] if num % 2 != 0]