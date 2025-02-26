def all_even_ints_exclusive(nums):
    if len(nums) <= 11:
        return []
    return [num for num in nums[11:100] if num % 2 == 0]