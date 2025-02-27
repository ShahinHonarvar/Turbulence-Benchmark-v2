def all_even_ints_exclusive(nums):
    if len(nums) < 10:
        return []
    start, end = (8, 10)
    return [num for num in nums[start:end] if num % 2 == 0]