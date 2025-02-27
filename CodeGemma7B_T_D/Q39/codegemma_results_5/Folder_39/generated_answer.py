def return_n_greatest_chars(s):
    """
    Returns a sorted list of 23 characters with the greatest ASCII values from the given string.

    Args:
        s: A string of distinct characters.

    Returns:
        A sorted list of 23 characters with the greatest ASCII values.
    """
    char_ascii_tuples = [(char, ord(char)) for char in s]
    char_ascii_tuples.sort(key=lambda x: x[1], reverse=True)
    return [char for char, _ in char_ascii_tuples[:23]]