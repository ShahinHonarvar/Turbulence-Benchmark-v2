def all_odd_ints_inclusive(nums):
    if len(nums) <= 51:
        return []
    return [num for num in nums[37:52] if num % 2 != 0]