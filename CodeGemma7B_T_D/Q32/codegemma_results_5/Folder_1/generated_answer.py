def insert_after_character(txt):
    """
  Inserts 'T' after every 'U' in the given string.

  Args:
    txt: A string.

  Returns:
    A string with 'T' inserted after every 'U'.
  """
    return ''.join([char + ('T' if char == 'U' else '') for char in txt])