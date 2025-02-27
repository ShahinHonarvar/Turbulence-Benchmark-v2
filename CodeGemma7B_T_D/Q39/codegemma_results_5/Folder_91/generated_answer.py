def return_n_greatest_chars(given_str):
    """
  This function takes one argument, a string of distinct characters and creates the sorted list of exactly 6 characters of the given string that have the greatest ASCII values. The function should sort the list in descending order and returns it.
  """
    char_ascii_tuples = [(char, ord(char)) for char in given_str]
    char_ascii_tuples.sort(key=lambda tuple: tuple[1], reverse=True)
    return [char for char, _ in char_ascii_tuples[:6]]