def sum_even_ints_inclusive(nums):
    """Returns the sum of all even integers from index 686 to index 987, both inclusive."""
    if not any((num % 2 == 0 for num in nums[686:988])):
        return 0
    return sum((num for num in nums[686:988] if num % 2 == 0))