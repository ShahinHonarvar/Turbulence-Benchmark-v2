def all_odd_ints_exclusive(nums):
    if len(nums) <= 90:
        return []
    return [num for num in nums[67:90] if num % 2 != 0]