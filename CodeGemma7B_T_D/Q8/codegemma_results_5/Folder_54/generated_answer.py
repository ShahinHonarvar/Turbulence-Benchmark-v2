def all_even_ints_exclusive(nums):
    if not nums:
        return []
    filtered_nums = [num for num in nums[27:34] if num % 2 == 0]
    return filtered_nums if filtered_nums else []