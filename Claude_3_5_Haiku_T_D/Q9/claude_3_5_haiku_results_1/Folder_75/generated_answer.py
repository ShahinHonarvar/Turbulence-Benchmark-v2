def all_odd_ints_inclusive(nums):
    if len(nums) <= 57:
        return []
    result = [num for num in nums[56:58] if num % 2 != 0]
    return result