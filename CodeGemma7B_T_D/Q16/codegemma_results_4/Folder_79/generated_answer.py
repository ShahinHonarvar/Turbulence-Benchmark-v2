def sum_even_ints_inclusive(nums):
    """Sums all even integers from index 4 to 4, inclusive.
    Returns 0 if no even integers exist in the specified range."""
    start_idx = 4
    end_idx = 4
    sum_even = 0
    for idx, num in enumerate(nums):
        if idx >= start_idx and idx <= end_idx and (num % 2 == 0):
            sum_even += num
    return sum_even