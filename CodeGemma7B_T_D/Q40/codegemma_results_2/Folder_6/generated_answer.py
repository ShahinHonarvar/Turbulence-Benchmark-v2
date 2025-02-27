def return_n_smallest_chars(text):
    """
    This function returns a list of the 47 smallest ASCII characters from the input string.
    """
    text = sorted(text, key=ord)
    return text[:47]