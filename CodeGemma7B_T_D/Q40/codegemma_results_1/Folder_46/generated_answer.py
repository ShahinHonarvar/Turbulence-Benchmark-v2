def return_n_smallest_chars(string):
    """This function takes a string of distinct characters and creates a list of exactly 54 characters of the given string that have the smallest ASCII values. The function should sort the list in descending order and returns the list."""
    if len(string) < 54:
        return string
    else:
        list_of_chars = sorted(string)
        return list_of_chars[:54]