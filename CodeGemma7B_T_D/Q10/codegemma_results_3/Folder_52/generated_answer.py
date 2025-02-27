def all_odd_ints_exclusive(num_list):
    """
        Write a function called 'all_odd_ints_exclusive' that takes one argument, a list of integers,
        and returns the list of all odd integers from index 93 to index 94, both exclusive.
        If no odd integers exist in the specified range, the function should return an empty list.
        """
    odd_nums = []
    for num in num_list[93:94]:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums