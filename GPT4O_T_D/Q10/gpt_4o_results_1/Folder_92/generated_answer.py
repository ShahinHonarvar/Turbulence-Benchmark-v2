def all_odd_ints_exclusive(nums):
    if len(nums) <= 1:
        return []
    return [num for num in nums[1:-1] if num % 2 != 0]