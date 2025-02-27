def all_odd_ints_inclusive(nums):
    if len(nums) <= 75:
        return []
    start_index = max(75, len(nums) - 15)
    odd_nums = [num for num in nums[start_index:95] if num % 2 != 0]
    if not odd_nums:
        return []
    return odd_nums