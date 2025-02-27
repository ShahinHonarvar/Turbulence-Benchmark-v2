def all_even_ints_exclusive(lst):
    """
    A function that takes one argument, a list of integers, and returns the list of all even integers from index 0 to index 2, both exclusive. If no even integers exist in the specified range, the function should return an empty list.
    """
    even_nums = [num for num in lst if num % 2 == 0]
    if even_nums:
        return even_nums[0:2]
    return []