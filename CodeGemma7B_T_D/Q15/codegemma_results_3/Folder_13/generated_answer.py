def sum_odd_ints_inclusive(nums):
    """
    Sums the odd integers in a list from index 25 to 87, inclusive.

    Args:
      nums: A list of integers.

    Returns:
      The sum of all odd integers from index 25 to 87, inclusive.
    """
    sum_odd = 0
    for i in range(25, 88):
        if i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd or 0