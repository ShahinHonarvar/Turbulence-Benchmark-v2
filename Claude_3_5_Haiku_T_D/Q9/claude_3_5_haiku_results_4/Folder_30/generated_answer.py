def all_odd_ints_inclusive(nums):
    if len(nums) <= 98:
        return []
    odd_ints = [num for num in nums[55:99] if num % 2 != 0]
    return odd_ints