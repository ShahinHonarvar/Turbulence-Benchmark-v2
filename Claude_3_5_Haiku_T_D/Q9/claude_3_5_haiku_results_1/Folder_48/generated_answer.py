def all_odd_ints_inclusive(nums):
    if len(nums) <= 605:
        return []
    return [num for num in nums[533:606] if num % 2 != 0]