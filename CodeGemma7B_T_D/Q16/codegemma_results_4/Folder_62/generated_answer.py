def sum_even_ints_inclusive(nums):
    """
    Sums all even integers from index 91 to index 99, inclusive.

    Args:
      nums: A list of integers.

    Returns:
      The sum of even integers from index 91 to index 99, inclusive.
    """
    sum = 0
    for i in range(91, 100):
        if i >= 91 and i <= 99:
            if nums[i] % 2 == 0:
                sum += nums[i]
    return sum