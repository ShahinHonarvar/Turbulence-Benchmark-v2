def all_odd_ints_exclusive(nums):
    """The function takes one argument, a list of integers, and
    returns the list of all odd integers from index 2 to index 7, both exclusive.
    If no odd integers exist in the specified range, the function should return an empty list."""
    result = []
    for i in range(2, 7):
        if nums[i] % 2:
            result.append(nums[i])
    return result