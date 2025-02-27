def all_odd_ints_exclusive(nums):
    if any((n % 2 for n in nums[389:748])):
        return [n for n in nums[389:748] if n % 2]
    return []