def all_odd_ints_exclusive(nums):
    if len(nums) < 72:
        return []
    odd_ints = [num for num in nums[70:72] if num % 2 != 0]
    return odd_ints