def sum_odd_ints_inclusive(nums):
    """
    Sums all odd integers from index 56 to index 98, inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    sum_odd = 0
    for i in range(56, 99):
        if i % 2 != 0:
            sum_odd += nums[i]
    if sum_odd == 0:
        return 0
    return sum_odd