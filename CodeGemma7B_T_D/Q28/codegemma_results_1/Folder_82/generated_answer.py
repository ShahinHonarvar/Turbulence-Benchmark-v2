def return_nth_smallest_ascii(s):
    """Return the caharacter with the 15th smallest ASCII value among those characters
       in the string that occur between indices 0 to 14, both inclusive."""
    return min(s[0:15], key=ord)