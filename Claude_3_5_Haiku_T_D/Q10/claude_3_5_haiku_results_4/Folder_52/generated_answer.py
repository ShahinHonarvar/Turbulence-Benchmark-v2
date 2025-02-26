def all_odd_ints_exclusive(nums):
    if len(nums) <= 95:
        return []
    result = [num for num in nums[94:95] if num % 2 != 0]
    return result