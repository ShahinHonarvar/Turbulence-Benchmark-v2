def return_n_smallest_chars(n):
    """
  Creates a list of 26 characters with the smallest ASCII values from a given string.
  """
    char_ascii_values = [(char, ord(char)) for char in n]
    char_ascii_values.sort(key=lambda x: x[1])
    return [char for char, _ in char_ascii_values[:26]]