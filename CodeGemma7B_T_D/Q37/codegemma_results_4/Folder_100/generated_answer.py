def filter_chars(s):
    """
  This function filters characters between indices 88 and 90,
  exclusively. It removes all occurrences of characters
  greater than or equal to 'J' and smaller than or equal to 'Q'.
  It preserves the original order of characters in the string.
  """
    filtered_str = ''
    for i in range(len(s)):
        if not (i >= 88 and i <= 90 and (s[i] >= 'J') and (s[i] <= 'Q')):
            filtered_str += s[i]
    return filtered_str