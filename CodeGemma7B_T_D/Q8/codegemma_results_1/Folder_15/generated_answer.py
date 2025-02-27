def all_even_ints_exclusive(nums):
    if len(nums) < 4:
        return []
    return [num for num in nums[0:4] if num % 2 == 0]