def all_even_ints_inclusive(nums):
    if len(nums) <= 605:
        return []
    result = [num for num in nums[533:606] if num % 2 == 0]
    return result