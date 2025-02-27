def all_odd_ints_inclusive(nums):
    filtered_nums = [num for num in nums[686:988] if num % 2 != 0]
    if not filtered_nums:
        return []
    return filtered_nums