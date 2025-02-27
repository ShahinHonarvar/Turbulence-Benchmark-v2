def sum_even_ints_inclusive(nums):
    """
    Write a function called sum_even_ints_inclusive that takes one argument, a list of integers,
    and returns the sum of all even integers from index 0 to index 8, both inclusive. If no even integers exist
    in the specified range, the function should return 0.

    Parameters:
        nums (list): A list of integers.

    Returns:
        int: The sum of all even integers from index 0 to index 8, both inclusive.
    """
    sum_even = 0
    for i in range(0, 9):
        if nums[i] % 2 == 0:
            sum_even += nums[i]
    return sum_even