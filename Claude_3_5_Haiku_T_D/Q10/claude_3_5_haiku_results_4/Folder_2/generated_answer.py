def all_odd_ints_exclusive(nums):
    if len(nums) <= 53:
        return []
    odd_nums = [num for num in nums[37:52] if num % 2 != 0]
    return odd_nums