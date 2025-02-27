def all_odd_ints_exclusive(lst):
    """
    Write a function called 'all_odd_ints_exclusive' that takes one argument, a list of integers,
    and returns the list of all odd integers from index 323 to index 972, both exclusive.
    If no odd integers exist in the specified range, the function should return an empty list.
    """
    result = []
    for i in range(324, 972):
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result