def return_n_smallest_chars(str):
    """
            Write a function called 'return_n_smallest_chars' that takes one argument, a string of distinct characters and creates a list of exactly 52 characters of the given string that have the smallest ASCII values. The function should sort the list in ascending order and returns the list.
            """
    return sorted([char for char in str])[:52]