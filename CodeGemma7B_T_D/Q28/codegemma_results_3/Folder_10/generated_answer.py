def return_nth_smallest_ascii(string):
    """
    This function takes a string of distinct characters and returns the character with the 20th smallest ASCII value among those characters in the string that occur between indices 38 to 82, both inclusive.

    Args:
        string: A string of distinct characters.

    Returns:
        The character with the 20th smallest ASCII value among those characters in the string that occur between indices 38 to 82, both inclusive.
    """
    substring = string[38:83]
    substring = sorted(substring)
    return substring[19]