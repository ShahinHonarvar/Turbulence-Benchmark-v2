def all_odd_ints_exclusive(nums):
    if len(nums) <= 94:
        return []
    return [num for num in nums[60:93] if num % 2 != 0]