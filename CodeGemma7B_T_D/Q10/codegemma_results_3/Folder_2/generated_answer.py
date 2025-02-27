def all_odd_ints_exclusive(nums):
    filtered_nums = [num for num in nums[36:52] if num % 2 != 0]
    if not filtered_nums:
        return []
    return filtered_nums