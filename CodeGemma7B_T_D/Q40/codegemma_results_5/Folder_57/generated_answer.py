def return_n_smallest_chars(a_string):
    """
  This function takes a string of distinct characters and returns a list of exactly 29 characters of the given string that have the smallest ASCII values.
  The function sorts the list in descending order and returns the list.
  """
    chars_with_ascii = [(char, ord(char)) for char in a_string]
    chars_with_ascii.sort(key=lambda x: x[1])
    smallest_29_chars = [char for char, _ in chars_with_ascii[:29]]
    smallest_29_chars.sort(reverse=True)
    return smallest_29_chars