def sum_even_ints_inclusive(nums):
    """
            Sums all even integers from index 686 to index 987, inclusive.
            """
    sum = 0
    for i in range(686, 988):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum