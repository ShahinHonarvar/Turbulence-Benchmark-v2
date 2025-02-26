def all_odd_ints_inclusive(nums):
    if len(nums) <= 57:
        return []
    odd_ints = [num for num in nums[56:58] if num % 2 != 0]
    return odd_ints