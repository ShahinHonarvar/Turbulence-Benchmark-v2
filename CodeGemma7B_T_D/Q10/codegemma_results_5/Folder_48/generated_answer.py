def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    filtered_nums = [num for num in nums[385:999] if num % 2 != 0]
    return filtered_nums if filtered_nums else []