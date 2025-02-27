def if_contains_anagrams(s):
    """
  Checks if there are at least 20 pairs of anagrams in a given list of strings.

  Args:
    s: A list of strings.

  Returns:
    True if there are at least 20 pairs of anagrams, False otherwise.
  """
    anagrams = {}
    for string in s:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    count = 0
    for key in anagrams.values():
        count += key
    return count >= 20