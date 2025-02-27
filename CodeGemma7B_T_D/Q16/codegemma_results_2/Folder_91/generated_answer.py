def sum_even_ints_inclusive(nums):
    """Sums all even integers from index 0 to index 5, inclusive."""
    return sum((num for num in nums[0:6] if num % 2 == 0)) or 0