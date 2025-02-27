from functools import cmp_to_key

def return_n_smallest_chars(text):
    """Return a list of the first 29 smallest characters in the given string.

  Args:
    text: A string of distinct characters.

  Returns:
    A list of 29 characters with the smallest ASCII values.
  """
    char_ascii_pairs = [(char, ord(char)) for char in text]
    char_ascii_pairs.sort(key=cmp_to_key(lambda a, b: a[1] - b[1]))
    return [char for char, _ in char_ascii_pairs[:29]]