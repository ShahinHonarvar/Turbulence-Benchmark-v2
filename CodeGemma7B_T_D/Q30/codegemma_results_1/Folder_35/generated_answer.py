def insert_before_character(string):
    """Inserts 'M' before '9'.

  Args:
    string: The string to insert 'M' before '9' in.

  Returns:
    The string with 'M' inserted before '9'.
  """
    if not string:
        return string
    return ''.join((c + 'M' if c == '9' else c for c in string))