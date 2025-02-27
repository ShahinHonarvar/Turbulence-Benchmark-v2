def all_even_ints_inclusive(nums):
    """Takes one argument, a list of integers, and returns the list of all even integers from index 0 to index 9, both inclusive. If no even integers exist in the specified range, the function should return an empty list."""
    res = []
    for i in range(10):
        if i % 2 == 0:
            res.append(i)
    return res