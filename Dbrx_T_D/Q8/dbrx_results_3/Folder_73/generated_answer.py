def all_even_ints_exclusive(nums):
    if len(nums) < 85:
        return []
    return [num for num in nums[36:85] if num % 2 == 0]