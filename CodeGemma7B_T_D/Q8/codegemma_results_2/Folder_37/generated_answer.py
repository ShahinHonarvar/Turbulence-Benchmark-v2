def all_even_ints_exclusive(nums):
    """Returns all even integers from index 1 to index 2, both exclusive."""
    return [num for num in nums[1:2] if num % 2 == 0]