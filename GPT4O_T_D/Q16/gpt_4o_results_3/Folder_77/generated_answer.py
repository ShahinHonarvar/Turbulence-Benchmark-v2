def sum_even_ints_inclusive(nums):
    if len(nums) < 539:
        return 0
    return sum((num for num in nums[527:539] if num % 2 == 0))