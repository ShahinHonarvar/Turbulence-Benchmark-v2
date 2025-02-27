def all_odd_ints_inclusive(nums):
    return [num for i, num in enumerate(nums[686:988], start=686) if num % 2 != 0]