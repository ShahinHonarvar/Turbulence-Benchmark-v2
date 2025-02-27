def return_nth_smallest_ascii(text):
    """Returns the character with the nth smallest ASCII value from text."""
    char_list = sorted(list(text))
    return char_list[4]