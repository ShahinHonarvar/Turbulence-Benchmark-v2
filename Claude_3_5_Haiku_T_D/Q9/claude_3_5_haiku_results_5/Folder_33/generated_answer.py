def all_odd_ints_inclusive(nums):
    if len(nums) <= 774:
        return []
    odd_ints = [num for num in nums[667:775] if num % 2 != 0]
    return odd_ints