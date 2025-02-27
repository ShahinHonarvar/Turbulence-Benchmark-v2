def filter_chars(string):
    """Filters characters between indices 33 and 70, inclusive, that are greater than or equal to '7' and smaller than or equal to 'k'.
  
  Args:
    string: The string to filter.
  
  Returns:
    The altered string with filtered characters removed.
  """
    filtered_string = ''
    for i in range(len(string)):
        if i < 33 or i > 70 or string[i] < '7' or (string[i] > 'k'):
            filtered_string += string[i]
    return filtered_string