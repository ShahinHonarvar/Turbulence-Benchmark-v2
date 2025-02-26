def all_even_ints_exclusive(nums):
    if len(nums) <= 93:
        return []
    return [num for num in nums[57:92] if num % 2 == 0]