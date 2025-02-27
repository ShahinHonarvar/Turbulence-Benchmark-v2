def return_n_greatest_chars(string):
    """
    Returns the sorted list of exactly 26 characters of the given string that have the greatest ASCII values.

    Args:
        string: A string of distinct characters.

    Returns:
        A sorted list of 26 characters with the greatest ASCII values.
    """
    char_ascii_tuples = [(char, ord(char)) for char in string]
    char_ascii_tuples.sort(key=lambda x: x[1], reverse=True)
    return [char for char, _ in char_ascii_tuples[:26]]