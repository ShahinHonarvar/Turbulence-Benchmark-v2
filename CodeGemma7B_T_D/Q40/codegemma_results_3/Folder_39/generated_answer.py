def return_n_smallest_chars(string):
    """
    Returns a list of the smallest 23 characters in the given string.
    
    Args:
    string: A string of distinct characters.
    
    Returns:
    A list of 23 characters sorted in ascending order of their ASCII values.
    """
    char_list = [(c, ord(c)) for c in string]
    char_list.sort(key=lambda x: x[1])
    n_smallest_chars = [char for char, _ in char_list[:23]]
    return n_smallest_chars