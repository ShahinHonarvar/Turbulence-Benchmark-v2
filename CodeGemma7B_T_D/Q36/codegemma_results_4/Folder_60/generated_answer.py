def filter_chars(s):
    """
  This function takes one argument, a string.
  For each character between the indices 23 and 83 (both exclusive) in the given string,
  if that character is greater than character 'f' and smaller than character 'o',
  the function should remove all occurrences of that character within the string
  while keeping the order of all characters in the string intact.
  The function should return the altered string.
  """
    for i in range(23, 83):
        if s[i] > 'f' and s[i] < 'o':
            while s[i] in s:
                s = s[:i] + s[i + 1:]
    return s