def all_odd_ints_exclusive(nums):
    if len(nums) < 573:
        return []
    odd_ints = [num for num in nums[295:573] if num % 2 != 0]
    return odd_ints