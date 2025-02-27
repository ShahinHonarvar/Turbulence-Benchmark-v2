def all_substring_of_size_n(given_string):
    """Returns a list of all distinct substrings of the length equal to n.

  Args: 
    given_string: A string from which substrings are to be generated.

  Returns:
    A list of all distinct substrings of the given length. It returns an empty 
    list if no such substrings exist in the given string.
  """
    final_result = set()
    for i in range(len(given_string) - 123):
        final_result.add(given_string[i:i + 124])
    return list(final_result)