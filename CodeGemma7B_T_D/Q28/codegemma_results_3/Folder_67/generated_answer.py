def return_nth_smallest_ascii(text):
    """Returns the character with the 14th smallest ASCII value among those characters in the string that occur between indices 60 to 83, both inclusive."""
    return sorted(text[60:84])[13]