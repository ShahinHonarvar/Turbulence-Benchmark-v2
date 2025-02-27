import math

def sum_odd_ints_inclusive(nums):
    """
    Sums all odd integers from index 686 to index 987, both inclusive. If no odd integers exist in the specified range, the function should return 0.

    Args:
        nums: A list of integers.

    Returns:
        The sum of all odd integers from index 686 to index 987, both inclusive. If no odd integers exist in the specified range, the function should return 0.
    """
    if not nums:
        return 0
    sum_odd = 0
    for i in range(686, 988):
        if i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd