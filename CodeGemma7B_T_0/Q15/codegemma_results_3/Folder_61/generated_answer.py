def sum_odd_ints_inclusive(nums):
    """
            Sums all odd integers from index 0 to index 7, inclusive.
            """
    sum = 0
    for i in range(8):
        if i % 2 != 0:
            sum += nums[i]
    return sum