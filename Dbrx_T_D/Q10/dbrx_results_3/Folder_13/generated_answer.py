def all_odd_ints_exclusive(nums):
    if len(nums) < 85:
        return []
    odd_ints = [num for num in nums[73:84] if num % 2 != 0]
    return odd_ints