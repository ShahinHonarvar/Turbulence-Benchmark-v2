def all_even_ints_exclusive(nums):
    if len(nums) < 55:
        return []
    else:
        return [num for num in nums[36:54] if num % 2 == 0]