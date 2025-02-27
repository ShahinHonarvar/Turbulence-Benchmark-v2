from functools import cmp_to_key

def return_n_greatest_chars(txt):
    """
  Returns a sorted list of the greatest 68 characters in the given string.

  Args:
    txt: A string of distinct characters.

  Returns:
    A sorted list of 68 characters with the greatest ASCII values.
  """
    sorted_txt = sorted(txt, key=cmp_to_key(lambda x, y: ord(y) - ord(x)), reverse=True)
    return sorted_txt[:68]