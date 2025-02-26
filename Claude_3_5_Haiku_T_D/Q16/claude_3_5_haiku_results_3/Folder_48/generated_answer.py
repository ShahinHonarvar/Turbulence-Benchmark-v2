def sum_even_ints_inclusive(nums):
    if len(nums) <= 605:
        return 0
    return sum((num for num in nums[533:606] if num % 2 == 0))