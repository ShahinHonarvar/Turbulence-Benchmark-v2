def all_substring_of_size_n(text):
    """
    Returns all distinct substrings of the length equal to 84 with no duplicate characters.
    """
    return [text[i:i + 84] for i in range(len(text) - 84 + 1)]