def return_n_smallest_chars(char_str):
    """
    Return the smallest ASCII characters to form a list of 85 characters
    """
    return sorted(char_str, key=ord, reverse=True)[:85]