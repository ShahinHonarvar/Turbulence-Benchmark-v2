def sum_even_ints_inclusive(nums):
    """
            Sums all even integers from index 209 to index 556, inclusive.
            """
    sum = 0
    for i in range(209, 557):
        if nums[i] % 2 == 0:
            sum += nums[i]
    if sum == 0:
        return 0
    return sum