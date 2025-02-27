def all_odd_ints_inclusive(nums):
    if len(nums) < 21:
        return []
    odd_ints = [num for num in nums[10:11] if num % 2 != 0]
    return odd_ints