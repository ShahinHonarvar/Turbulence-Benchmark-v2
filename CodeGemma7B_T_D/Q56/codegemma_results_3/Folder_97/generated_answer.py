def all_substring_of_size_n(text):
    """Function to return the list of all substrings of the length equal to 142 with no duplicate characters.

  Args:
    text: The string to extract substrings from.

  Returns:
    A list of all unique substrings of length 142 from the given string or an empty list.
  """
    all_substrs = []
    for start in range(len(text) - 142 + 1):
        substring = text[start:start + 142]
        if len(set(substring)) == len(substring):
            all_substrs.append(substring)
    return all_substrs