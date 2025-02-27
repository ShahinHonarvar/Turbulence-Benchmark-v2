def sum_odd_ints_inclusive(nums):
    """Calculates the sum of all odd integers from index 262 to index 746, inclusive."""
    sum_odd_numbers = 0
    for i in range(262, 747):
        if i % 2 != 0:
            sum_odd_numbers += nums[i]
    return sum_odd_numbers