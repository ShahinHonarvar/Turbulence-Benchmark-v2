def return_n_smallest_chars(text):
    """
    sorts and returns list of characters in ascending order of ASCII values
    in descending order
    """
    return sorted(text, key=ord, reverse=True)[:84]