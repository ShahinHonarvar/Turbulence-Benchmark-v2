def all_even_ints_exclusive(lst):
    """
            Write a function called 'all_even_ints_exclusive' that takes one argument, a list of integers, \\
                and returns the list of all even integers from index 78 to index 93, both exclusive. If no \\
                even integers exist in the specified range, the function should return an empty list.
            """
    result = []
    for i in range(78, 93):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result