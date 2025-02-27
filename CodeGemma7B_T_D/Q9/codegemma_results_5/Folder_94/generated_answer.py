def all_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums[28:41] if num % 2 != 0]
    if not odd_nums:
        return []
    return odd_nums