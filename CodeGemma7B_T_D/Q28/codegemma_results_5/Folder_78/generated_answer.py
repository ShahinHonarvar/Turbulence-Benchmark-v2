def return_nth_smallest_ascii(s):
    """
  Returns the character with the 14th smallest ASCII value among those characters in the string that occur between indices 0 to 87, both inclusive.

  Args:
    s: A string of distinct characters.

  Returns:
    The character with the 14th smallest ASCII value.
  """
    sorted_chars = sorted(s)
    valid_chars = sorted_chars[0:88]
    valid_chars.sort(key=ord)
    return valid_chars[13]