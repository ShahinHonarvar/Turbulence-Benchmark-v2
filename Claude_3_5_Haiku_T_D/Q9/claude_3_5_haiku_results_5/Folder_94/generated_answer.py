def all_odd_ints_inclusive(nums):
    if len(nums) <= 40:
        return []
    odd_ints = [num for num in nums[28:41] if num % 2 != 0]
    return odd_ints