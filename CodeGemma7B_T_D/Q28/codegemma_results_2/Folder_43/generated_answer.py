def return_nth_smallest_ascii(string):
    """Return the character with the 11th smallest ASCII value among those characters in the string that occur between indices 14 to 35, both inclusive."""
    return min(string[13:35 + 1])[0]