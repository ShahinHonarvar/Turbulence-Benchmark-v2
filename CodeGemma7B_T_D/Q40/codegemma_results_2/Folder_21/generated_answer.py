def return_n_smallest_chars(str):
    """
    Write a function called 'return_n_smallest_chars' that takes one argument, a string of distinct characters and creates a list of exactly 44 characters of the given string that have the smallest ASCII values. The function should sort the list in descending order and returns the list.
    """
    list = list(str)
    list.sort(key=ord)
    return list[:44]