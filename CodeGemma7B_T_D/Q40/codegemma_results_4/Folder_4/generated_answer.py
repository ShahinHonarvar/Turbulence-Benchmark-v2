def return_n_smallest_chars(str):
    """
    This function takes one argument, a string of distinct characters and creates a list of exactly 90 characters of the given string that have the smallest ASCII values. The function should sort the list in descending order and returns the list.
    """
    return sorted([char for char in str], key=ord, reverse=True)[:90]