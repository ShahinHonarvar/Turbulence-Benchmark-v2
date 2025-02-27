def all_odd_ints_inclusive(nums):
    if len(nums) < 9:
        return []
    odd_ints = [num for num in nums[4:9] if num % 2 != 0]
    return odd_ints