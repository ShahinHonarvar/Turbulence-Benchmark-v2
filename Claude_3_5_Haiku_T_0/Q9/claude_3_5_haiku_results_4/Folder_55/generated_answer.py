def all_odd_ints_inclusive(nums):
    if len(nums) <= 10:
        return []
    result = [num for num in nums[10:11] if num % 2 != 0]
    return result