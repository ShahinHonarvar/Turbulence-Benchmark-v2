def all_even_ints_exclusive(nums):
    if not nums:
        return []
    filtered_nums = [num for num in nums if num % 2 == 0 and 13 < num < 76]
    return filtered_nums or []