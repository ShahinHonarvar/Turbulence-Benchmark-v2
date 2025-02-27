def sum_odd_ints_inclusive(lst):
    """
            Sums all odd integers from index 1 to index 1, inclusive.

            Args:
                lst: A list of integers.

            Returns:
                The sum of all odd integers from index 1 to index 1, inclusive. If no odd integers exist in the specified range, the function should return 0.
            """
    sum = 0
    for i in range(1, len(lst) + 1):
        if i % 2 != 0:
            sum += lst[i - 1]
    return sum