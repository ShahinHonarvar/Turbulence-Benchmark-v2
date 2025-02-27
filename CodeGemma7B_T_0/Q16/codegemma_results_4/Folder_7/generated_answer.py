def sum_even_ints_inclusive(nums):
    """
            Sums all even integers from index 661 to index 924, inclusive.
            """
    sum = 0
    for i in range(661, 925):
        if i in range(661, 925) and nums[i] % 2 == 0:
            sum += nums[i]
    return sum